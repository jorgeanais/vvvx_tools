from pathlib import Path
from utils.runner import run

"""
This program extract the galactic coordinates limits of each
fits files and save it to output.csv
This is done in parallel using the multiprocess module.
"""

def main():
    data_dir = Path("/run/media/jorge/TWOTERAS/DATA/phd/PSF_bulge/")
    run(data_dir)


if __name__ == "__main__":
    main()
