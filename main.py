import networkx as nx
import matplotlib.pyplot as plt
import random

#performs the transaction for the shortest path. If possible transaction then updates teh graph and returns true else prints error
#message
def try_alternative_paths(G, src, dest, transaction_amt):
    # Try the shortest path as an alternative
    shortest_path = nx.shortest_path(G, source=src, target=dest, weight='weight')
    feasible_transaction = all(G[u][v]['weight'] >= transaction_amt for u, v in zip(shortest_path, shortest_path[1:]))
    if feasible_transaction:
        for u, v in zip(shortest_path, shortest_path[1:]):
            G[u][v]['weight'] -= transaction_amt
        return True
    else:
        print("Shortest path transaction failed due to insufficient capacity.")
        return False

#Using a pre built graph: https://networkx.org/documentation/stable/auto_examples/graph/plot_karate_club.html#sphx-glr-auto-examples-graph-plot-karate-club-py 
G = nx.karate_club_graph()

# Add random weights to edges to represent channel capacities
for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 100)

# Number of transactions to perform
num_transactions = int(input("Enter number of transactions: "))

for transaction in range(num_transactions):
    # Now I will choose a random src and dest from the list of nodes from the grapgh
    src = random.choice(list(G.nodes))
    dest = random.choice(list(G.nodes))
    print(f"\nTransaction {transaction + 1}: The src is {src}, and the dest is {dest}.")

    # First, try the widest path
    paths = nx.all_simple_paths(G, source=src, target=dest)
    widest_path = max(paths, key=lambda path: min(G[u][v]['weight'] for u, v in zip(path, path[1:])), default=None)

    # If the widest path is found and feasible, use it
    if widest_path:
        transaction_amt = random.randint(0, 10)
        if all(G[u][v]['weight'] >= transaction_amt for u, v in zip(widest_path, widest_path[1:])):
            for u, v in zip(widest_path, widest_path[1:]):
                G[u][v]['weight'] -= transaction_amt
        else:
            print("Widest path transaction failed due to insufficient capacity.")
            # Try alternative paths
            if not try_alternative_paths(G, src, dest, transaction_amt):
                print("All transaction attempts failed.")

# Display the updated capacities on the edges
print("\nCapacities after transactions:")
for u, v in G.edges():
    capacity = G[u][v]['weight']
    print(f"Edge ({u}, {v}): {capacity}")

# Display the final graph after all transactions
nx.draw(G, with_labels=True)
plt.title("Final Graph with Capacities")
plt.show()
