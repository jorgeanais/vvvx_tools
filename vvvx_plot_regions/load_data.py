import numpy as np
import pandas as pd


def angle_separation(a: float, b: float):
    """Return the angular separation between two angles in degrees."""
    

# Read input data
column_names = ("tile_id", "l_min", "l_max", "l_widht", "l_middle", "b_min", "b_max", "b_widht", "b_middle")
tile_df = pd.read_csv("output.csv", names=column_names, dtype={"tile_id": np.int32})





# Draw coordinates in the region of interst

# Approach using ligo skymap
# https://lscsoft.docs.ligo.org/ligo.skymap/
# import ligo.skymap.plot
# import matplotlib.pyplot as plt
# ax = plt.axes(projection='galactic zoom', center='0d 0d', radius='20 deg', rotate='10 deg')
# ax.grid()
 