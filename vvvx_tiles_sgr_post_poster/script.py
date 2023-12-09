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
    "data/tiles_vvvx_poster_only.csv",
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


# /home/jorge/Dropbox/develop/vvvx_tools/vvvx_tiles_sgr_post_poster/data/complete_psf_vvvbulge.csv
# data/tiles_vvv_poster.csv
# Load data Bulge
df_bulge = pd.read_csv(
    "data/complete_psf_vvvbulge.csv",
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
df_vvvx = pd.read_csv(
    "data/tiles_VVVX.csv",
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

df_vvvx_area = pd.read_csv(
    "data/VVVX_regions_minnitiPullen.csv"
)

df_vvv_area = pd.read_csv(
    "data/VVV_regions_minnitiPullen.csv"
)

ax = plt.subplot(projection="galactic zoom", center='0d 0d', radius='30 deg', rotate='0 deg')
ax.grid()

# Gaia source density (optional)
#hdu = fits.open("../vvvx_plot_regions/density_map.fits")[1]
#hdu.header["COORDSYS"] = "GALACTIC"
#ax.imshow_hpx(hdu, cmap="Greys")

# Regiones VVV
for index, row in df_vvv_area.iterrows():
    r = Quadrangle(
        (row["l_min"], row["b_min"]) * u.deg,
        row["l_widht"] * u.deg,
        row["b_widht"] * u.deg,
        edgecolor="steelblue",
        facecolor="none", # (1,0,0,0.5)
        linestyle="solid",  # ‘solid’ | ‘dashed’, ‘dashdot’, ‘dotted’
        linewidth=2.5, 
        transform=ax.get_transform("galactic"),
    )
    ax.add_patch(r)
    # ax.text(row["l_middle"], row["b_middle"], row["region"], horizontalalignment='center', transform=ax.get_transform('galactic'))

# REgiones VVVX
for index, row in df_vvvx_area.iterrows():
    r = Quadrangle(
        (row["l_min"], row["b_min"]) * u.deg,
        row["l_widht"] * u.deg,
        row["b_widht"] * u.deg,
        edgecolor="steelblue",
        facecolor="none", # (1,0,0,0.5)
        linestyle="dashed",  # ‘solid’ | ‘dashed’, ‘dashdot’, ‘dotted’
        linewidth=2.5, 
        transform=ax.get_transform("galactic"),
    )
    ax.add_patch(r)
    # ax.text(row["l_middle"], row["b_middle"], row["region"], horizontalalignment='center', transform=ax.get_transform('galactic'))


for index, row in df.iterrows():
    r = Quadrangle(
        (row["l_min"], row["b_min"]) * u.deg,
        row["l_widht"] * u.deg,
        row["b_widht"] * u.deg,
        edgecolor="darkturquoise",
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
        edgecolor="salmon",  # springgreen
        facecolor="none",
        transform=ax.get_transform("galactic"),
    )
    ax.add_patch(r)
    ax.text(row["l_middle"], row["b_middle"], str(int(row["tile_id"])), horizontalalignment='center', transform=ax.get_transform('galactic'))
    
for index, row in df_vvvx.iterrows():
    r = Quadrangle(
        (row["l_min"], row["b_min"]) * u.deg,
        row["l_widht"] * u.deg,
        row["b_widht"] * u.deg,
        edgecolor="springgreen",  # 
        facecolor="none",
        transform=ax.get_transform("galactic"),
    )
    ax.add_patch(r)
    ax.text(row["l_middle"], row["b_middle"], str(int(row["tile_id"])), horizontalalignment='center', transform=ax.get_transform('galactic'))
    


# Add Sgr stream nominal position
plot_sgr_stream_nom_position(ax)
ax.plot(5.607, -14.087, c="red", marker="x", markersize=10, linewidth=3, transform=ax.get_transform("galactic"))

ax.invert_xaxis()
ax.invert_yaxis()
ax.set_xlabel("Galactic longitude (deg)")
ax.set_ylabel("Galactic latitude (deg)")
plt.show()
