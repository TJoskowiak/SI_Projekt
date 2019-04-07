import networkx as nx
import matplotlib.pyplot as plt


class GraphDrawer:
    def __init__(self):
        self.edges = []
        self.colors = []

    def add_node(self, label, color):
        pass

    def add_edge(self, label_a, label_b, color):
        flag = True
        for edge in self.edges:
            if edge[0] == label_a:
                flag = False
        if flag:
            self.colors.append(color)

        self.edges.append((label_a, label_b))

    def draw_graph(self):
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge[0], edge[1])

        nx.draw(G, node_color=self.colors, node_size=800)
        plt.show()


if __name__ == "__main__":
    gd = GraphDrawer()

    gd.add_edge(1, 2, 1)
    gd.add_edge(2, 3, 1)
    gd.add_edge(3, 4, 3)
    gd.add_edge(4, 5, 1)
    gd.add_edge(5, 1, 2)
    gd.add_edge(1, 4, 2)
    gd.add_edge(1, 3, 2)

    gd.draw_graph()
