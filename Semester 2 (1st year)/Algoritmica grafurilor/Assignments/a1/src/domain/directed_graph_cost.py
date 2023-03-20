from src.domain.directed_graph import DirectedGraph


class DirectedGraphCost(DirectedGraph):
    def __init__(self, numberOfVertices):
        super().__init__(numberOfVertices)

        self.__costs = {}

    def addEdge(self, edgeToAdd: tuple, cost=0):
        super().addEdge(edgeToAdd)
        self.__costs[edgeToAdd] = cost
