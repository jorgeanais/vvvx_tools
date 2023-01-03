import ligo.skymap.plot
import matplotlib.pyplot as plt
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.io import fits
from astropy.visualization.wcsaxes import Quadrangle
from astropy.wcs import WCS
from matplotlib.patches import Rectangle

"""
This script produces a plot of the VVVX fingerprint region with the Gaia density map
as background.

Reference:
https://docs.astropy.org/en/stable/visualization/wcsaxes/overlays.html
https://lscsoft.docs.ligo.org/ligo.skymap/
https://lscsoft.docs.ligo.org/ligo.skymap/plot/allsky.html
"""

ax = plt.subplot(projection="galactic mollweide")
ax.grid()

# Gaia source density
hdu = fits.open("/home/jorge/Dropbox/develop/vvvx_plot_regions/density_map.fits")[1]
hdu.header["COORDSYS"] = "GALACTIC"
ax.imshow_hpx(hdu, cmap="Greys")

# 2MASS all-sky source density
# (not working because healpix is not in galactic coordinates)
#
# twomass_df = pd.read_csv(
#     "twomass_allskt_healpix.csv", dtype={"hpx9": int, "counts": float}
# )
# twomass_df_fixed = (
#     twomass_df.set_index("hpx9")
#     .reindex(range(0, 3145728))
#     .fillna(0)
#     .reset_index()
#     .astype(int)
# )
# twomass_array = twomass_df_fixed["counts"].values
# print(twomass_array.shape)
# ax.imshow_hpx(twomass_array, cmap="Greys")


# Rectangles
df = pd.read_csv(
    "output.csv",
    names=(
        "tile_id",
        "l_min",
        "l_max",
        "l_widht",
        "l_middle",
        "b_min",
        "b_max",
        "b_widht",
        "b_middle",
    ),
    dtype={"tile_id": int},
)
for index, row in df.iterrows():
    r = Quadrangle(
        (row["l_middle"], row["b_middle"]) * u.deg,
        row["l_widht"] * u.deg,
        row["b_widht"] * u.deg,
        edgecolor="red",
        facecolor="none",
        transform=ax.get_transform("galactic"),
    )
    ax.add_patch(r)

# r = Quadrangle((0, -15)*u.deg, 1.5*u.deg, 2.0*u.deg, edgecolor='red', facecolor='none', transform=ax.get_transform('galactic'))
# ax.add_patch(r)


plt.show()
