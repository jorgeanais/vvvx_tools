import ligo.skymap.plot
import matplotlib.pyplot as plt
import pandas as pd
from astropy import units as u

from astropy.io import fits
from astropy.visualization.wcsaxes import Quadrangle


def plot_sgr_stream_nom_position(ax: plt.Axes) -> None:
    """Plot the nominal position of the Sgr stream on the given axis."""

    from sgr_coords import sgr_stream_gal

    ax.plot(sgr_stream_gal.l.deg, sgr_stream_gal.b.deg, c="red", linestyle="dashed", transform=ax.get_transform("galactic"))



# Load data
df = pd.read_csv(
    "../vvvx_tileid/tiles_id.csv",
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

# Load data Bulge
df_bulge = pd.read_csv(
    "../vvv_explorer/output_vvv_bulge.csv",
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

ax = plt.subplot(projection="galactic zoom", center='0d 0d', radius='30 deg', rotate='0 deg')
ax.grid()

# Gaia source density (optional)
hdu = fits.open("../vvvx_plot_regions/density_map.fits")[1]
hdu.header["COORDSYS"] = "GALACTIC"
ax.imshow_hpx(hdu, cmap="Greys")


for index, row in df.iterrows():
    r = Quadrangle(
        (row["l_min"], row["b_min"]) * u.deg,
        row["l_widht"] * u.deg,
        row["b_widht"] * u.deg,
        edgecolor="salmon",
        facecolor="none",
        transform=ax.get_transform("galactic"),
    )
    ax.add_patch(r)
    ax.text(row["l_middle"], row["b_middle"], str(int(row["tile_id"])), horizontalalignment='center', transform=ax.get_transform('galactic'))

for index, row in df_bulge.iterrows():
    r = Quadrangle(
        (row["l_min"], row["b_min"]) * u.deg,
        row["l_widht"] * u.deg,
        row["b_widht"] * u.deg,
        edgecolor="springgreen",
        facecolor="none",
        transform=ax.get_transform("galactic"),
    )
    ax.add_patch(r)
    ax.text(row["l_middle"], row["b_middle"], str(int(row["tile_id"])), horizontalalignment='center', transform=ax.get_transform('galactic'))

# Add Sgr stream nominal position
plot_sgr_stream_nom_position(ax)
ax.plot(5.607, -14.087, c="red", marker="x", markersize=10, transform=ax.get_transform("galactic"))

ax.invert_xaxis()
ax.invert_yaxis()
plt.show()