import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def calculateQ(d):
    r = d.shape[0]
    q = pd.DataFrame(np.zeros((r, r)))
    for i in range(r):
        for j in range(r):
            if i == j:
                q.iloc[i, j] = 0
            else:
                sumI = d.iloc[i].sum()
                sumJ = d.iloc[j].sum()
                q.iloc[i, j] = (r-2) * d.iloc[i, j] - sumI - sumJ
    return q

def findLowestPair(q):
    r = q.shape[0]
    minVal = float('inf')
    minIndex = (0, 0)
    for i in range(r):
        for j in range(i, r):
            if q.iloc[i, j] < minVal:
                minVal = q.iloc[i, j]
                minIndex = (i, j)
    return minIndex

def doDistOfPairMembersToNewNode(i, j, d):
    r = d.shape[0]
    sumI = d.iloc[i].sum()
    sumJ = d.iloc[j].sum()
    
    denominator = 2. * (r - 2.)
    if denominator == 0:
        return (0, 0)  # Return (0, 0) when the denominator is zero to avoid division by zero error

    dfu = (1. / denominator) * ((r - 2.) * d.iloc[i, j] + sumI - sumJ)
    dgu = (1. / denominator) * ((r - 2.) * d.iloc[i, j] - sumI + sumJ)

    return (dfu, dgu)

def calculateNewDistanceMatrix(f, g, d):
    r = d.shape[0]
    nd = pd.DataFrame(np.zeros((r-1, r-1)))

    # Copy over the old data to this matrix
    ii = jj = 1
    for i in range(r):
        if i == f or i == g:
            continue
        for j in range(r):
            if j == f or j == g:
                continue
            nd.iloc[ii, jj] = d.iloc[i, j]
            jj += 1
        ii += 1
        jj = 1
            
    # Calculate the first row and column
    ii = 1
    for i in range(r):
        if i == f or i == g:
            continue
        nd.iloc[0, ii] = round((d.iloc[f, i] + d.iloc[g, i] - d.iloc[f, g]) / 2., 3)
        nd.iloc[ii, 0] = round((d.iloc[f, i] + d.iloc[g, i] - d.iloc[f, g]) / 2., 3)
        ii += 1

    return nd

def doNeighbourJoining(d, log_file):
    joins = []
    nodes = list(range(d.shape[0]))  # List of node labels (initially 0 to n-1)
    next_node = d.shape[0]  # Label for the next new node
    
    G = nx.Graph()
    G.add_nodes_from(nodes)

    while d.shape[0] > 1:
        q = calculateQ(d)
        lowestPair = findLowestPair(q)
        i = lowestPair[0]
        j = lowestPair[1]
        pairDist = doDistOfPairMembersToNewNode(i, j, d)

        log_file.write(f"Joining nodes {nodes[i],pairDist[0]} and {nodes[j],pairDist[1]}\n")
        log_file.write("Distances before join:\n")
        log_file.write(d.to_string() + "\n")
        log_file.write("\n")

        
        joins.append((nodes[i], nodes[j], pairDist))

        new_node = next_node
        next_node += 1

        # Add nodes and edges to the graph
        G.add_node(new_node)
        G.add_edge(new_node, nodes[i], weight=pairDist[0])
        G.add_edge(new_node, nodes[j], weight=pairDist[1])

        # Replace the joined nodes with the new node in the nodes list
        nodes.remove(nodes[i])
        nodes.remove(nodes[j-1])  
        nodes.append(new_node)

        # Update the distance matrix
        d = calculateNewDistanceMatrix(i, j, d)

    return joins, G

def run(distMatrix):
    with open("joins_and_distances.txt", "w") as log_file:
        joins, G = doNeighbourJoining(distMatrix, log_file)
    
        # Write joins to a text file
        with open("joins.txt", "w") as f:
            for join in joins:
                f.write(f"Joining nodes {join[0]} and {join[1]} with distances {join[2]}\n")

        # Draw the tree
        plt.figure(figsize=(16, 10))  # Increase the figure size further as needed
        pos = nx.spring_layout(G)  # Positions for all nodes
        labels = nx.get_edge_attributes(G, 'weight')
        rounded_labels = {k: round(v, 3) for k, v in labels.items()}  # Round distances to 3 decimal places
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=rounded_labels)
        plt.title('Neighbor Joining Tree')
        plt.savefig("neighbor_joining_tree.png")
        plt.show()

if __name__ == "__main__":
    distMatrix = pd.DataFrame(
        [
            [0, 0.17, 0.59, 0.59, 0.77, 0.81, 0.87],
            [0.17, 0, 0.6, 0.59, 0.77, 0.82, 0.86],
            [0.59, 0.6, 0, 0.13, 0.75, 0.73, 0.86],
            [0.59, 0.59, 0.13, 0, 0.75, 0.74, 0.88],
            [0.77, 0.77, 0.75, 0.75, 0, 0.8, 0.93],
            [0.81, 0.82, 0.73, 0.74, 0.8, 0, 0.9],
            [0.87, 0.86, 0.86, 0.88, 0.93, 0.9, 0]
        ]
    )
    run(distMatrix)
       
