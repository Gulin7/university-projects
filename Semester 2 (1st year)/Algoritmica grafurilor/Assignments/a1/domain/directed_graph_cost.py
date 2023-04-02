from domain.directed_graph_no_cost import DirectedGraph


class DirectedGraphCost(DirectedGraph):
    def __init__(self, number_of_vertices):
        super().__init__(number_of_vertices)

        self.__costs = {}

    # def add_edge(self, edge_to_add: tuple, cost):
    #     super().add_edge(edge_to_add)

