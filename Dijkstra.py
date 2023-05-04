import networkx as nx
import matplotlib.pyplot as plt


class Dijkstra:
    def __init__(self):
        self.graph = nx.Graph()
        edges = [('A', 'B', 5),
                 ('A', 'H', 8),
                 ('A', 'E', 9),
                 ('B', 'D', 15),
                 ('B', 'C', 12),
                 ('B', 'H', 4),
                 ('H', 'E', 5),
                 ('H', 'F', 6),
                 ('H', 'C', 7),
                 ('E', 'F', 4),
                 ('E', 'G', 20),
                 ('C', 'D', 3),
                 ('C', 'F', 1),
                 ('C', 'G', 11),
                 ('F', 'G', 13),
                 ('D', 'G', 9)]
        self.graph.add_weighted_edges_from(edges)

    @staticmethod
    def draw_graph(graph):
        positions = nx.spring_layout(graph)
        nx.draw_networkx_nodes(graph, positions, node_size=1500, alpha=.9, node_color='#0000ac')
        nx.draw_networkx_edges(graph, positions, width=2, alpha=.5, edge_color='k', style='dashed')
        nx.draw_networkx_labels(graph, positions, font_size=24, font_color='white')
        edge_weight_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos=positions, edge_labels=edge_weight_labels)
        plt.show()

    def find_path_between_A_and_G(self):
        path = nx.dijkstra_path(self.graph, 'A', 'G')
        print(path)

    def shortest_path_tree(self):
        shortest_paths = nx.single_source_dijkstra_path(self.graph, 'A')
        shortest_path_tree = nx.Graph()
        for path in shortest_paths.values():
            for i in range(1, len(path)):
                source = path[i - 1]
                target = path[i]
                weight = self.graph.get_edge_data(source, target)['weight']
                shortest_path_tree.add_edge(source, target, weight=weight)
        Dijkstra.draw_graph(shortest_path_tree)


def test_dijkstra():
    dijkstra = Dijkstra()
    dijkstra.shortest_path_tree()


test_dijkstra()
