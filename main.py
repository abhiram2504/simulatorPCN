import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

# creating a simple graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (2, 3),
                    (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)])

options = {
    'node_color': 'red',
    'node_size': 100,
    'width': 3,
    'with_labels': True,
    'font_weight': 'bold',
    'font_color': 'white',
    'font_size': 10,
    'edge_color': 'black',
    'arrows': True,
    'arrowsize': 12,
}

nx.draw_networkx(G, **options)
plt.show()
