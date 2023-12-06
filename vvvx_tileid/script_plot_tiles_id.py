import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd



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


fig, ax = plt.subplots()
ax.plot([0, 100],[-20, 20])

for i, row in df.iterrows():
    print(i)
    anchor_point = (row["l_min"], row["b_min"])
    width = row["l_widht"]
    height = row["b_widht"]
    x_middle = row["l_middle"]
    y_middle = row["b_middle"]
    tile_id = str(int(row["tile_id"]))

    print(anchor_point, width, height)

    rectangle = Rectangle(anchor_point, width, height, fill=False, edgecolor="red")
    ax.add_patch(rectangle)

    #ax.text(x_middle, y_middle, tile_id)

ax.set_axis_off()
plt.show()