import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def initialize_graph():
    G = nx.karate_club_graph()

    # Add random weights to edges to represent channel capacities
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, 100)

    print("\nCapacities before transactions:")
    for u, v in G.edges():
        capacity = G[u][v]['weight']
        print(f"Edge ({u}, {v}): {capacity}")

    return G

def initialize_demand_matrix(num_nodes):
    demand_matrix = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        # Generate random probabilities that sum up to 1
        probabilities = np.random.dirichlet(np.ones(num_nodes - 1), size=1).flatten()
        for j in range(num_nodes):
            if i != j:
                demand_matrix[i, j] = probabilities[j - (j > i)]  # Adjust the indexing
    return demand_matrix

def perform_transaction(G, src, dest, transaction_amt):
    path_probabilities = np.array(demand_matrix[src, :])
    path_probabilities[dest] = 0  # Exclude self-loop
    path_probabilities /= path_probabilities.sum()  # Normalize probabilities to sum to 1
    chosen_path = np.random.choice(range(num_nodes), p=path_probabilities)

    widest_path = find_widest_path(G, src, chosen_path)

    if widest_path and all(G[u][v]['weight'] >= transaction_amt for u, v in zip(widest_path, widest_path[1:])):
        for u, v in zip(widest_path, widest_path[1:]):
            G[u][v]['weight'] -= transaction_amt
        return True
    else:
        print("Widest path transaction failed due to insufficient capacity.")
        return try_shortest_paths(G, src, dest, transaction_amt)

def find_widest_path(G, src, dest):
    paths = nx.all_simple_paths(G, source=src, target=dest)
    return max(paths, key=lambda path: min(G[u][v]['weight'] for u, v in zip(path, path[1:])), default=None)

def main():
    global num_nodes, demand_matrix
    num_nodes = 32  # Set the number of nodes
    G = initialize_graph()
    demand_matrix = initialize_demand_matrix(num_nodes)

    print("\nGenerated Demand Matrix:")
    print(demand_matrix)

    num_transactions = int(input("Enter the number of transactions to route: "))
    for _ in range(num_transactions):
        src = random.choice(range(num_nodes))
        dest = random.choice(range(num_nodes))
        while src == dest:
            dest = random.choice(range(num_nodes))

        if demand_matrix[src, dest] > 0:
            transaction_amt = demand_matrix[src, dest] * random.randrange(1,31)  # Use the probability as the transaction amount
            print(f"\nTransaction: Source={src}, Destination={dest}, Amount={transaction_amt}")
            if not perform_transaction(G, src, dest, transaction_amt):
                print("All transaction attempts failed.")
        else:
            print(f"No demand from {src} to {dest}, skipping transaction.")

    print("\nCapacities after transactions:")
    for u, v in G.edges():
        capacity = G[u][v]['weight']
        print(f"Edge ({u}, {v}): {capacity}")

    nx.draw(G, with_labels=True)
    plt.title("Final Graph with Capacities")
    plt.show()

main()
