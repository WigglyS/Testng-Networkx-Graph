import networkx
import matplotlib.pyplot as plt
import random
import scipy

w = 10
h = 10
d = 70
plt.figure(figsize=(w, h), dpi=d)

GraphInitialSize = 20
G = networkx.path_graph(0)
num = 0;
w = 0;

#adds some random nodes and edges
for i in range(1,GraphInitialSize):
    num = random.randrange(0,GraphInitialSize)
    w = random.randrange(1,10)
    G.add_edges_from([(i, num)])
    G[i][num]['weight'] = w

    w = random.randrange(1, 10)
    G.add_edges_from([(i, i-1)])
    G[i][i-1]['weight'] = w



labels = [0, 1, 2, 3, 4, 5]

#printing for the node based graph implimentation
pos = networkx.spring_layout(G)
networkx.draw_networkx_nodes(G, pos, node_size=700)
networkx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
networkx.draw_networkx_edges(G, pos, width=6)
labels = networkx.get_edge_attributes(G, 'weight')
networkx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print(networkx.dijkstra_path(G, 0, GraphInitialSize-1))
print(networkx.astar_path(G, 0, GraphInitialSize-1))
T=networkx.minimum_spanning_tree(G)
print(sorted(T.edges(data=True)))
A = networkx.adjacency_matrix(G,nodelist=sorted(G.nodes()))
print(A.todense())


plt.axis ("off")
plt.show()
plt.savefig("out.png")




