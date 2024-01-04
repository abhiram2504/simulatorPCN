import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

# Function to generate a random traffic demand matrix
def generate_traffic_demand_matrix(nodes):
    demand_matrix = np.random.randint(1, 100, size=(len(nodes), len(nodes)))
    np.fill_diagonal(demand_matrix, 0)  # Set diagonal elements to zero to represent no self-transaction
    return demand_matrix

def try_shortest_paths(G, src, dest, transaction_amt):
    shortest_path = nx.shortest_path(G, source=src, target=dest, weight='weight')
    feasible_transaction = all(G[u][v]['weight'] >= transaction_amt for u, v in zip(shortest_path, shortest_path[1:]))
    
    if feasible_transaction:
        for u, v in zip(shortest_path, shortest_path[1:]):
            G[u][v]['weight'] -= transaction_amt
        return True
    else:
        print("Shortest path transaction failed due to insufficient capacity.")
        return False

G = nx.karate_club_graph()
nodes = list(G.nodes)

# Add random weights to edges to represent channel capacities
for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 100)

# Generate traffic demand matrix
traffic_demand_matrix = generate_traffic_demand_matrix(nodes)

print("\nCapacities before transactions:")
for u, v in G.edges():
    capacity = G[u][v]['weight']
    print(f"Edge ({u}, {v}): {capacity}")

num_transactions = int(input("Enter number of transactions: "))

for transaction in range(num_transactions):
    src = random.choice(nodes)
    dest = random.choice(nodes)
    
    # Use traffic demand matrix to determine transaction amount
    transaction_amt = traffic_demand_matrix[nodes.index(src)][nodes.index(dest)]
    
    print(f"\nTransaction {transaction + 1}: Src={src}, Dest={dest}, Amount={transaction_amt}")

    paths = nx.all_simple_paths(G, source=src, target=dest)
    widest_path = max(paths, key=lambda path: min(G[u][v]['weight'] for u, v in zip(path, path[1:])), default=None)

    if widest_path:
        if all(G[u][v]['weight'] >= transaction_amt for u, v in zip(widest_path, widest_path[1:])):
            for u, v in zip(widest_path, widest_path[1:]):
                G[u][v]['weight'] -= transaction_amt
        else:
            print("Widest path transaction failed due to insufficient capacity.")
            if not try_shortest_paths(G, src, dest, transaction_amt):
                print("All transaction attempts failed.")

print(traffic_demand_matrix)

print("\nCapacities after transactions:")
for u, v in G.edges():
    capacity = G[u][v]['weight']
    print(f"Edge ({u}, {v}): {capacity}")

nx.draw(G, with_labels=True)
plt.title("Final Graph with Capacities")
plt.show()
