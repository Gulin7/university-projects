from src.domain.graph import *


class Ui:
    def __init__(self):
        pass

    def showMenu(self):
        print("""           🧧MENU🧧
1️⃣ Get number of vertices.
2️⃣ Show all vertices.
3️⃣ Check if an edge exists.
4️⃣ Get in/out degree.
5️⃣ Show inBound edges.
6️⃣ Show outBound edges.
7️⃣ Add vertex.
8️⃣ Remove vertex.
9️⃣ Add edge.
🔟 Remove edge.
1️⃣1️⃣ Read graph from standard file.
1️⃣2️⃣ Read graph from file 2.
1️⃣3️⃣ Write graph to file.
1️⃣4️⃣ Generate a random graph.
1️⃣5️⃣ Show all edges.
1️⃣6️⃣Get connected components.
0️⃣ Exit. """)

    def getCommand(self):
        """
        Gets a command input from the user.

        :return: int
        """
        command = 0
        while True:
            try:
                command = int(input("Enter a command: "))
                if command < 0 or command > 16:
                    print("Invalid command!🙅‍♂️")
                else:
                    break
            except ValueError as ve:
                print("Invalid command! 👎" + str(ve))
        return command

    def getVertex(self):
        """
        Gets a vertex input from the user.

        :return: int
        """
        vertex = 0
        while True:
            try:
                vertex = int(input("Enter a vertex: "))
                break
            except ValueError as ve:
                print("Invalid vertex!🙅‍♀️ " + str(ve))
        return vertex

    def getCost(self):
        """
        Gets the cost from a user.

        :return: int
        """
        cost = 0
        while True:
            try:
                cost = int(input("Enter a cost: "))
                break
            except ValueError as ve:
                print("Invalid cost! " + str(ve))
        return cost

    def getEdge(self):
        start = 0
        end = 0
        while True:
            try:
                start = int(input("Enter start edge: "))
                end = int(input("Enter end edge: "))
                break
            except ValueError as ve:
                print("Invalid edge! " + str(ve))
        edge = (start, end)
        return edge

    def getEdgeCost(self):
        start = 0
        end = 0
        cost = 0
        while True:
            try:
                start = int(input("Enter start edge: "))
                end = int(input("Enter end edge: "))
                cost = int(input("Enter ost: "))
                break
            except ValueError as ve:
                print("Invalid edge! 🙅‍♀️" + str(ve))
        edge = (start, end)
        return edge, cost

    def getFileName(self):
        filename = input("Enter the name of a file: ")
        return filename

    def getNumberOfVertices(self):
        numberOfVertices = 0
        while True:
            try:
                numberOfVertices = int(input("Enter number of vertices: "))
                if numberOfVertices < 1:
                    print("Invalid number of vertices!🙅‍♀️")
                else:
                    return numberOfVertices
            except ValueError as ve:
                print("Invalid number of vertices! 👎 " + str(ve))

    def getNumberOfEdges(self):
        numberOfEdges = 0
        while True:
            try:
                numberOfEdges = int(input("Enter number of Edges: "))
                if numberOfEdges < 1:
                    print("Invalid number of Edges!🙅‍♀️")
                else:
                    return numberOfEdges
            except ValueError as ve:
                print("Invalid number of Edges!🙅‍♂️ " + str(ve))

    def runUi(self):
        command = 0
        graph = readGraphFromFileStandard('graph100k.txt')
        graph = readGraphFromFile2('small_graph2')
        while True:
            self.showMenu()
            command = self.getCommand()
            if command == 0:
                print("You left the app!")
                break
            elif command == 1:
                # get number of vertices
                numberOfVertices = graph.getNumberOfVertices()
                print(f"The number of vertices is {numberOfVertices} !")
            elif command == 2:
                # get set of vertices
                setOfVertices = graph.getSetOfVertices()
                print(f"The set of vertices is: \n {setOfVertices} !")
            elif command == 3:
                # check if an edge exists
                edge = self.getEdge()
                outcome = graph.isEdge(edge)
                if outcome:
                    print(f"The edge {edge} exists!")
                else:
                    print(f"The edge {edge} does not exist!")
            elif command == 4:
                # in/out Degree
                vertex = self.getVertex()
                inDegree = graph.getInDegree(vertex)
                outDegree = graph.getOutDegree(vertex)
                print(f"""The in degree is: {inDegree}
The out degree is: {outDegree}""")
            elif command == 5:
                # inBound edges
                vertex = self.getVertex()
                print(f"The outbound edges for the vertex {vertex} are: ")
                for vertexIn in graph.dictIn[vertex]:
                    edge = (vertex, vertexIn)
                    print(f"Edge: {edge} ")
            elif command == 6:
                # outBound edges
                vertex = self.getVertex()
                print(f"The outbound edges for the vertex {vertex} are: ")
                for vertexOut in graph.dictOut[vertex]:
                    edge = (vertex, vertexOut)
                    print(f"Edge: {edge} ")
            elif command == 7:
                # add vertex
                vertex = self.getVertex()
                checkExist = graph.isVertex(vertex)
                if checkExist:
                    print("Vertex already exists!")
                else:
                    graph.addVertex(vertex)
                    print("Vertex added!")
            elif command == 8:
                # remove vertex
                vertex = self.getVertex()
                checkExist = graph.isVertex(vertex)
                if not checkExist:
                    print("Vertex does not exist!")
                else:
                    graph.removeVertex(vertex)
                    print("Vertex removed!")
            elif command == 9:
                # add edge
                edge, cost = self.getEdgeCost()
                checkExist = graph.isEdge(edge)
                if checkExist:
                    print("Edge already exists!")
                else:
                    print("Edge added")
                    graph.addEdge(edge)
            elif command == 10:
                # remove edge
                edge = self.getEdge()
                checkExist = graph.isEdge()
                if checkExist:
                    graph.removeEdge(edge)
                    print("Edge removed!")
                else:
                    print("Edge does not exist!")
            elif command == 11:
                # read standard
                filename = self.getFileName()
                graph = readGraphFromFileStandard(filename)
                print("Graph read!")
            elif command == 12:
                # read 2
                filename = self.getFileName()
                graph = readGraphFromFile2(filename)
                print("Graph read!")
            elif command == 13:
                # write to file
                filename = self.getFileName()
                copyGraph = graph.createCopy()
                copyGraph = writeGraphToFile(filename, graph)
                print("Graph successfully written!")
            elif command == 14:
                # gen random
                numberOfVertices = self.getNumberOfVertices()
                numberOfEdges = self.getNumberOfEdges()
                graph = generateRandomGraph(numberOfVertices, numberOfEdges)
                print("Graph successfully generated!")
            elif command == 15:
                # show all edges
                print(f"{graph.getAllEdges()}")
            elif command == 16:
                listOfComponents = graph.getConnectedComponents()
                for graphComponent in listOfComponents:
                    print(f"{graphComponent.getAllEdges()}")

