from astropy.table import Table
from pathlib import Path


def cal2fits(calfile: Path, output_dir: Path) -> None:
    """Convert a .cals file to a .fits file"""

    print(f"Processing {calfile.name}")

    t = Table.read(calfile, format="ascii")
    t.write(output_dir / calfile.with_suffix(".fits"), format="fits")
