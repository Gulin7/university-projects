from random import randint


class UndirectedGraph:
    def __init__(self, numberOfVertices=0):
        self.__dictIn = {}
        self.__dictOut = {}
        for index in range(numberOfVertices):
            self.__dictIn[index] = []
            self.__dictOut[index] = []

    @property
    def dictIn(self):
        return self.__dictIn

    @property
    def dictOut(self):
        return self.__dictOut

    def isVertex(self, vertexToCheck: int):
        """
        Checks if a vertex exists or not.
        :param vertexToCheck: int, represents a vertex
        :return: bool
        """
        if vertexToCheck not in self.__dictIn.keys():
            return False
        return True

    def addVertex(self, vertexToAdd: int):
        if self.isVertex(vertexToAdd):
            raise ValueError('Vertex already in graph!')

        self.__dictIn[vertexToAdd] = []
        self.__dictOut[vertexToAdd] = []

    def removeVertex(self, vertexToRemove: int):
        if not self.isVertex(vertexToRemove):
            raise ValueError('Vertex does not exist!')
        # REMOVE COSTS FOR ALL THE EDGES THAT CONTAIN THE VERTEX WE REMOVE
        inEdges = self.getInBoundEdges(vertexToRemove)
        outEdges = self.getOutBoundEdges(vertexToRemove)

        for vertex in self.__dictOut[vertexToRemove]:
            self.__dictIn[vertex].remove(vertexToRemove)
        for vertex in self.__dictIn[vertexToRemove]:
            self.__dictOut[vertex].remove(vertexToRemove)

        del self.__dictIn[vertexToRemove]
        del self.dictOut[vertexToRemove]

    def isEdge(self, edgeToCheck: tuple):
        start = edgeToCheck[0]
        end = edgeToCheck[1]

        # If one of the vertexes does not exist => not and Edge
        if not self.isVertex(start) or not self.isVertex(end):
            return False

        # We check if start is a predecessor to end and if end is a successor to start.

        if start not in self.__dictIn[end] or end not in self.__dictOut[start]:
            return False

        return True

    def addEdge(self, edgeToAdd: tuple):
        start = edgeToAdd[0]
        end = edgeToAdd[1]

        if self.isEdge(edgeToAdd):
            return

        self.__dictOut[start].append(end)
        self.__dictOut[end].append(start)
        #
        self.__dictIn[start].append(end)
        self.__dictIn[end].append(start)

    def removeEdge(self, edgeToRemove: tuple):
        if not self.isEdge(edgeToRemove):
            raise ValueError('Edge does not exist!')

        start, end = edgeToRemove

        self.__dictIn[end].remove(start)
        self.__dictOut[start].remove(end)

    def getNumberOfVertices(self):
        """

        :return:
        """
        return len(self.__dictIn)

    def getSetOfVertices(self):
        """

        :return:
        """
        return list(self.__dictIn.keys())

    def getInDegree(self, vertex: int):
        """

        :param vertex:
        :return:
        """
        if not self.isVertex(vertex):
            raise ValueError('Vertex not in graph!')
        return len(self.__dictIn[vertex])

    def getOutDegree(self, vertex: int):
        """

        :param vertex:
        :return:
        """
        if not self.isVertex(vertex):
            raise ValueError('Vertex not in graph!')
        return len(self.__dictOut[vertex])

    def getInBoundEdges(self, vertex: int):
        """

        :param vertex:
        :return:
        """
        edges = []
        for inVertex in self.__dictIn[vertex]:
            edges.append((inVertex, vertex))
        return edges

    def getOutBoundEdges(self, vertex: int):
        """

        :param vertex:
        :return:
        """
        edges = []
        for outVertex in self.__dictOut[vertex]:
            edges.append((vertex, outVertex))
        return edges

    def getAllEdges(self):
        """

        :return:
        """
        edges = []
        for vertex in self.getSetOfVertices():
            for edge in self.getOutBoundEdges(vertex):
                edges.append(edge)
        return edges

    def createCopy(self):
        copiedGraph = UndirectedGraph()

        for vertex in self.getSetOfVertices():
            copiedGraph.addVertex(vertex)

        for vertex in self.getSetOfVertices():
            for edge in self.getInBoundEdges(vertex):
                copiedGraph.addEdge(edge)

        return copiedGraph

    def getConnectedComponents(self):
        listOfComponents = []
        copiedGraph = self.createCopy()
        # We will use the copied graph to create new graphs
        while copiedGraph.getNumberOfVertices() != 0:
            newGraph = UndirectedGraph()
            # we get a starting vertex
            startVertex = copiedGraph.getSetOfVertices()[0]
            queueList = [startVertex]
            newGraph.addVertex(startVertex)
            position = 0

            ok = True
            while ok:
                if position == len(queueList):
                    break
                ok = False
                for vertex in self.__dictOut[queueList[position]]:
                    ok = True
                    if vertex not in queueList:
                        queueList.append(vertex)
                        newGraph.addVertex(vertex)
                    newGraph.addEdge((queueList[position], vertex))

                position += 1

            listOfComponents.append(newGraph)

            for vertex in queueList:
                try:
                    copiedGraph.removeVertex(vertex)
                except ValueError as ve:
                    pass

        return listOfComponents


def readGraphFromFileStandard(filename: str):
    file = open(filename, 'rt')

    numberOfVertices, numberOfEdges = [int(x) for x in file.readline().strip().split()]
    graph = UndirectedGraph(numberOfVertices)

    for index in range(numberOfEdges):
        start, end, cost = map(int, file.readline().strip().split())
        edge = (start, end)
        try:
            graph.addEdge(edge)
        except ValueError as ve:
            pass

    # print(graph.dictIn)
    # print(graph.dictOut)

    file.close()

    return graph


def readGraphFromFile2(filename: str):
    file = open(filename, 'rt')

    graph = UndirectedGraph()

    for line in file.readlines():
        lineCheck = line.strip().split()
        if len(lineCheck) == 1:
            graph.addVertex(int(lineCheck[0]))
        else:
            start, end = map(int, lineCheck)
            edge = (start, end)
            if not graph.isVertex(start):
                graph.addVertex(start)
            if not graph.isVertex(end):
                graph.addVertex(end)
            graph.addEdge(edge)
    return graph


def writeGraphToFile(filename: str, graph: UndirectedGraph):
    file = open(filename, 'wt')

    for vertex in graph.getSetOfVertices():
        # check if isolated
        if graph.getInDegree(vertex) == 0 and graph.getOutDegree(vertex) == 0:
            file.write(str(vertex) + '\n')
        else:
            for vertexOut in graph.dictOut[vertex]:
                edge = (vertex, vertexOut)
                file.write(f'{vertex} {vertexOut}\n')

    file.close()


def generateRandomGraph(numberOfVertices: int, numberOfEdges: int):
    graph = UndirectedGraph(numberOfVertices)

    while numberOfEdges != 0:
        start = randint(0, numberOfVertices - 1)
        end = randint(0, numberOfVertices - 1)
        edge = (start, end)
        try:
            graph.addEdge(edge )
            numberOfEdges -= 1
        except ValueError:
            continue

    return graph
