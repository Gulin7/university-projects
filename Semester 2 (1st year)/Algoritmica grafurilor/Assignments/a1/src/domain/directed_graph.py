class DirectedGraph:
    def __init__(self, numberOfVertices=0):
        self.__dictIn = {}
        self.__dictOut = {}

        for index in range(numberOfVertices):
            # we are creating the 2 lists for each node
            self.__dictIn[index] = []
            self.__dictOut[index] = []

    def getDictIn(self):
        return self.__dictIn

    def getDictOut(self):
        return self.__dictOut

    def isVertex(self, vertexToCheck):
        return vertexToCheck in self.__dictIn.keys()

    def addVertex(self, vertexToAdd):
        """
        Adds a vertex to the directed graph. Basically it gives the key vertexToAdd an empty list as value
        in both dictIn and dictOut.

        :param vertexToAdd: int, vertex that we want to add
        :return: none
        """
        if self.isVertex(vertexToAdd):
            raise ValueError('Vertex already exists!')

        self.__dictIn[vertexToAdd] = []
        self.__dictOut[vertexToAdd] = []

    def removeVertex(self, vertexToRemove):
        """
        Removes a vertex from the directed graph. It first deletes vertexToRemove for each other vertex that goes in
        or comes out of vertexToRemove and then it deletes the key vertexToRemove from dictIn and dictOut.

        :param vertexToRemove: int, vertex that is removed
        :return: none
        """
        if not self.isVertex(vertexToRemove):
            raise ValueError('Vertex does not exist!')

        # for each vertex that goes in vertexToRemove, we delete vertexToRemove from that ones vertex dictOut ( nodes that
        # it goes into
        for vertex in self.__dictIn[vertexToRemove]:
            self.__dictOut[vertex].pop(vertexToRemove)

        # Analogy for dictOut
        for vertex in self.__dictOut[vertexToRemove]:
            self.__dictIn[vertex].pop(vertexToRemove)

        del self.__dictIn[vertexToRemove]
        del self.__dictOut[vertexToRemove]

    def isEdge(self, edgeToCheck: tuple):
        """
        Checks if an edge exists.

        :param edgeToCheck: tuple, 2 ints, representing the start vertex and end vertex
        :return: bool
        """
        startVertex = edgeToCheck[0]
        endVertex = edgeToCheck[1]

        # first we check if startVertex and endVertex exist
        if not self.isVertex(startVertex) or not self.isVertex(endVertex):
            return False

        if startVertex not in self.__dictIn[endVertex]:
            return False

        if endVertex not in self.__dictOut[startVertex]:
            return False

        return True

    def addEdge(self, edgeToAdd: tuple):
        """
        Adds an edge to the graph.


        :param edgeToAdd: tuple, 2 ints, the edge that is added
        :return: none
        """
        startVertex = edgeToAdd[0]
        endVertex = edgeToAdd[1]

        if self.isEdge(edgeToAdd):
            raise ValueError('Edge already exists!')

    def removeEdge(self, edgeToRemove: tuple):
        """
        Removes and edge from the graph.

        :param edgeToRemove: tuple, 2 ints, the edge that is removed
        :return: none
        """
        startVertex = edgeToRemove[0]
        endVertex = edgeToRemove[1]

        if not self.isEdge(edgeToRemove):
            raise ValueError('Edge does not exist!')

    def getNumberOfVertices(self):
        return len(self.getDictIn())

    def getSetOfVertices(self):
        return self.getDictIn().keys()
