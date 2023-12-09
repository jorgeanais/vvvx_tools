import itertools

from astropy.table import Table
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from shapely import box


# Load the file containing the info of each tile
df = pd.read_csv(
    "data/test.csv",
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

tiles = df.set_index("tile_id").apply(lambda row: box(row['l_min'], row['b_min'], row['l_max'], row['b_max']), axis=1).to_dict()


# Create a graph
graph = nx.Graph()

# Add all nodes
for tile_id in list(tiles.keys()):
    graph.add_node(tile_id)

# Add edges
edges = []
for tile_id_1, tile_id_2 in itertools.combinations(tiles, r=2):
    # tuple[int, int]
    if tiles[tile_id_1].intersects(tiles[tile_id_2]):
        # print(tile_id_1, tile_id_2)
        graph.add_edge(tile_id_1, tile_id_2)
        edges.append((tile_id_1, tile_id_2))

[print(e) for e in edges]


# Graph Coloring
coloring = nx.greedy_color(graph, strategy="largest_first")

# Save results to a csv file
df["coloring"] = df["tile_id"].map(coloring)

df.to_csv("output_with_coloring.csv", index=False)


# Visualize the graph with colors
pos = nx.spring_layout(graph)
node_colors = [coloring[node] for node in graph.nodes]
nx.draw(graph, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, font_color="white")
plt.savefig("test.png")