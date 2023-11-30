'''
This uses a random graph
num_nodes = 10
#this is the probability between an edge
probability = 0.4
G_temp = nx.random_graphs.erdos_renyi_graph(num_nodes, probability)

Goal is to check how we can use comman randomesses for routing. 

Demand matrix. How much each person wants to send to another perosn.

Look into routing policies. Measeure the success rate of transactions. 
'''

import networkx as nx
import matplotlib.pyplot as plt
import random

# Use a pre-built weighted graph (karate club graph in this case)
#this is an inbuild grapgh
G = nx.karate_club_graph()

# Add random weights to edges to represent channel capacities
for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)

# Number of transactions to perform
num_transactions = 5

for transaction in range(num_transactions):
    # Now I will choose a random src and dest
    src = random.choice(list(G.nodes))
    dest = random.choice(list(G.nodes))
    print(f"\nTransaction {transaction + 1}: The src is {src}, and the dest is {dest}.")

    # Shortest path b/w src and dest
    shortest_path = nx.shortest_path(G, source=src, target=dest, weight='weight')

    transaction_amt = random.randint(0,10)

    # Check if transaction is feasible based on channel capacities
    feasible_transaction = all(G[u][v]['weight'] >= transaction_amt for u, v in zip(shortest_path, shortest_path[1:]))

    if feasible_transaction:
        # Update balance for the edge between src and dest
        for u, v in zip(shortest_path, shortest_path[1:]):
            G[u][v]['weight'] -= transaction_amt

       

    else:
        print("Transaction failed due to insufficient capacity.")

 # Display the updated capacities on the edges
print("Capacities after transaction:")
for u, v in G.edges():
    capacity = G[u][v]['weight']
    print(f"Edge ({u}, {v}): {capacity}")

# Display the final graph after all transactions
nx.draw(G, with_labels=True)
plt.title("Final Graph with Capacities")
plt.show()

