import numpy as np
from astropy.table import Table, hstack, vstack
from astropy.table.column import MaskedColumn, Column
from astropy.coordinates import SkyCoord
from astropy import units as u


table_1 = Table.read(
    "/home/jorge/Documents/data/vvvx/jhk0439.fits",
    format='fits',
)

table_2 = Table.read(
    "/home/jorge/Documents/data/vvvx/jhk0453.fits",
    format='fits',
)



ct1 = SkyCoord(table_1["ra"], table_1["dec"], unit=(u.deg, u.deg))
ct2 = SkyCoord(table_2["ra"], table_2["dec"], unit=(u.deg, u.deg))

idx_t1, d2d_t1, d3d = ct1.match_to_catalog_sky(ct2)