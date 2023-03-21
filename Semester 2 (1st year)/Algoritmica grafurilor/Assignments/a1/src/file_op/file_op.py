from random import randint

from src.domain.directed_graph import DirectedGraph


def readGraphFromStandardFile(filename: str):
    """
    This reads a graph from a standard file! the ones with the following format:
    numberOfVertices NumberOfEdges
    startVertex endVertex
    ... and so on

    :param filename: str, name of the file we are reading from
    :return:
    """
    file = open(filename, 'r')

    numberOfVertices, numberOfEdges = [int(element) for element in file.readline().strip().split()]

    graph = DirectedGraph(numberOfVertices)

    for index in range(numberOfEdges):
        startVertex, endVertex = map(int, file.readline().strip().split())
        graph.addEdge((startVertex, endVertex))

    print(graph.getDictIn())
    print(graph.getDictOut())

    file.close()
    return graph


def generateRandomGraph(numberOfVertices: int, numberOfEdges: int):
    """
    Generates a random graph.

    :param numberOfVertices: int, number of vertices in the randomly generated graph
    :param numberOfEdges: int, number of edges in the randomly generated graph
    :return: DirectedGraph
    """
    graph = DirectedGraph(numberOfVertices)

    while numberOfEdges > 0:
        startVertex = randint(0, numberOfVertices - 1)
        endVertex = randint(0, numberOfVertices - 1)
        edge = (startVertex, endVertex)
        try:
            graph.addEdge(edge)
            numberOfEdges -= 1
        except ValueError as ve:
            print(str(ve))

    return graph


def writeGraphToFile(graph: DirectedGraph, filename: str):
    """
    Writes a graph into a file, using the following format

    vertex vertex ... vertex
    startVertex endVertex
    ... and so on

    :param graph: DirectedGraph, the graph we are writing into the file
    :param filename: str, the name of the file we are writing into
    :return: none
    """

    setOfVertices = [str(vertex) for vertex in graph.getSetOfVertices()]

    file = open(filename, 'w')
    file.write(' '.join(setOfVertices))

    for edge in graph.getAllEdges():
        file.write(f'{edge[0]} {edge[1]}\n')

    file.close()


def readGraphFromSelfMadeFile(filename: str):
    """
    Reads a graph from a self made file, with the non standard format.

    :param filename: str, the name of the file we are reading from
    :return: DirectedGraph, the graph we read from the given file
    """

    file = open(filename, 'r')
    graph = DirectedGraph()

    for vertex in file.readline().strip().split():
        try:
            graph.addVertex(int(vertex))
        except ValueError:
            raise ValueError('Invalid file!')

    for line in file.readlines():
        startVertex, endVertex = line.strip().split()
        edge = (startVertex, endVertex)
        try:
            graph.addEdge(edge)
        except ValueError:
            raise ValueError('Invalid file!')

    return graph
