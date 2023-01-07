import ligo.skymap.plot
import matplotlib.pyplot as plt
import pandas as pd
from astropy import units as u

from astropy.visualization.wcsaxes import Quadrangle


# Load data
df = pd.read_csv(
    "tiles_id.csv",
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

for index, row in df.iterrows():
    r = Quadrangle(
        (row["l_min"], row["b_min"]) * u.deg,
        row["l_widht"] * u.deg,
        row["b_widht"] * u.deg,
        edgecolor="red",
        facecolor="none",
        transform=ax.get_transform("galactic"),
    )
    ax.add_patch(r)
    ax.text(row["l_middle"], row["b_middle"], str(int(row["tile_id"])), horizontalalignment='center', transform=ax.get_transform('galactic'))

ax.invert_xaxis()
ax.invert_yaxis()
plt.show()