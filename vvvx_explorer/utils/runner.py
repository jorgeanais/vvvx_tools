import ctypes
import multiprocessing as mp
from multiprocessing.sharedctypes import RawArray, Value
import numpy as np
from pathlib import Path
import pandas as pd

import utils.process as process


def run(data_dir: Path) -> None:

    file_list = list(data_dir.glob("jhk*.fits"))
    
    n_parameters = 9  # TODO: I should get this from the function
    n_output = len(file_list)  # number_of_files
    
    
    output = (RawArray(ctypes.c_double, n_parameters * n_output), (n_output, n_parameters))
    counter = Value('i', 0)

    with mp.Pool(initializer=process.check_limits_init, initargs=(output, counter)) as pool:
        pool.starmap(process.check_limits, enumerate(file_list))

    ouitput_array = np.ctypeslib.as_array(output[0]).reshape(output[1])
    pd.DataFrame(ouitput_array).to_csv("output.csv", index=False, header=False)
    print(counter.value, "files processed")  # TODO: delete this line
    print(ouitput_array.shape)  # TODO: delete this line