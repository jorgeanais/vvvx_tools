import numpy as np
from pathlib import Path

from multiprocessing.sharedctypes import RawArray, Value

from astropy.coordinates import SkyCoord
from astropy.table import Table
import pandas as pd


def check_limits_init(
    output: tuple[RawArray, tuple[int, int]],
    counter: int
) -> None:
    """
    Initializer to transform a RawArray into a 2D Numpy array
    used to store the results of a computation.
    This function is called once when each child process is created

    `output`: contains the raw array and the shape of the output
              numpy array. array[0] is number of parameters, 
              array[1] is the number of records (rows)
    `counter`: index of the current process
    """
    
    global gbl_output, gbl_counter

    # Make the counter globally available to the children process
    gbl_counter = counter

    # Convert the RawArray into a Numpy array with the right shape
    gbl_output = np.ctypeslib.as_array(output[0])
    gbl_output = gbl_output.reshape(output[1])


def check_limits(idx: int, filepath: Path):
    """
    Worker function for multiprocessing.
    Check limits of a catalog and store the results in a global array.
    """

    def get_min_max_widht_middle(angles: np.ndarray) -> tuple[float, float, float, float]:
        """
        Get the minimum and maximum angle taking into consideration that 360 deg = 0 deg
        Assuming that maximum angular difference is lower than 90 deg
        """

        min_angle = np.min(angles)
        max_angle = np.max(angles)
        width =  max_angle - min_angle
        middle = (min_angle + max_angle) / 2.0
        
        # Straight forward case
        if max_angle - min_angle < 180.0:
            return min_angle, max_angle, width, middle
        
        # Warped case
        shifted_angles = np.where(angles > 180.0, angles - 360.0, angles)
        min_angle = np.min(shifted_angles)
        max_angle = np.max(shifted_angles)
        width =  max_angle - min_angle
        middle = (min_angle + max_angle) / 2.0
        middle = middle if middle >= 0 else middle + 360


        return min_angle + 360, max_angle, width, middle

    
    print("Processing file ", filepath.stem, " with process ", idx)  # TODO: remove

    try:
        df = Table.read(filepath, format="ascii").to_pandas()
    except Exception as e:
        print("Error reading file", filepath.stem, e)
        print() 
    
    coords = SkyCoord(df["ra"], df["dec"], unit=("deg", "deg"))
    df["l"] = coords.galactic.l.deg
    df["b"] = coords.galactic.b.deg

    tile_id = float(filepath.stem[-3:])

    lmin, lmax, lwidht, lmiddle = get_min_max_widht_middle(df.l.values)
    bmin = df.b.min()
    bmax = df.b.max()
    bwidht = bmax - bmin
    bmiddle = (bmin + bmax) / 2.0

    gbl_output[idx, :] = np.array([tile_id, lmin, lmax, lwidht, lmiddle, bmin, bmax, bwidht, bmiddle])
    with gbl_counter.get_lock():
        gbl_counter.value += 1
