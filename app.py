import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    G = nx.Graph()


    G.add_edges_from([(1, 2),
                      (2, 3),
                      (3, 4),
                      (4, 1),
                      (4, 5),
                      (5, 6),
                      (6, 2)])
    print(G.nodes())
    print(G.edges())


    colors = [1,2,1,1,1,1]

    nx.draw(G, node_color=colors, node_size=800)
    plt.show()