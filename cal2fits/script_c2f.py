import multiprocessing as mp
from pathlib import Path

from utils.proc import cal2fits


data_dir = Path("/home/jorge/Documents/data/vvvxtiles/raw/VVV_Bulge_poslon_upperSgr2")
output_dir = Path("/home/jorge/Documents/data/vvvxtiles/raw/VVV_Bulge_poslon_upperSgr3")

file_list = list(data_dir.glob("zyjhk*.cals"))
args = [(file, output_dir) for file in file_list]


with mp.Pool(8) as pool:
    pool.starmap(cal2fits, args)
