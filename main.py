import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

# creating a simple graph
G = nx.Graph()




'''
This uses a random graph
num_nodes = 10
#this is the probability between an edge
probability = 0.4
G_temp = nx.random_graphs.erdos_renyi_graph(num_nodes, probability)
'''

G = nx.Graph()

# Add nodes (at least 5 nodes)
nodes = [1, 2, 3, 4, 5, 6]
G.add_nodes_from(nodes)

# Add edges to make it a complete graph
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        G.add_edge(nodes[i], nodes[j], balance = 20)


edges_to_remove = [(1, 2), (3, 4), (3,6), (2,5)]
G.remove_edges_from(edges_to_remove)

#Now I will choose a random src and dest
src = random.choice(nodes)
dest = random.choice(nodes)
print(f"The src is: {src}, and the dest is: {dest}.")

#shortest path b/w src and dest
shortest_path = nx.shortest_path(G, source=src, target=dest)

tranaction_amt = 10
if len(shortest_path) > 1:
    # Update balance for the edge between src and dest
    for i in range(len(shortest_path) - 1):
        u, v = shortest_path[i], shortest_path[i + 1]
        G[u][v]['balance'] -= tranaction_amt

    # Display the updated balances on the edges
    print(f"Balances after transaction:")
    for u, v in G.edges():
        balance = G[u][v]['balance']
        print(f"Edge ({u}, {v}): {balance}")


nx.draw(G, with_labels=True)
plt.title("Graph")
plt.show()


