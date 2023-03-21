from src.file_op.file_op import *
from src.domain.directed_graph import DirectedGraph
from src.domain.directed_graph_cost import DirectedGraphCost


class Ui:
    def __init__(self):
        self.graph = DirectedGraph()

    def showMenu(self):
        print("""           🧧MENU🧧
1. Read graph from a standard file
2. Read graph from a self made file
3. Write graph into a file
4. Add a vertex
5. Remove a vertex
6. Add an edge
7. Remove an edge
8. Display graph
9. Exit 
""")

    def getCommand(self):
        while True:
            try:
                command = int(input('Enter a command: '))
                if command > 9 or command < 1:
                    print('Invalid command!')
                else:
                    break
            except ValueError:
                print('Invalid command!')
        return command

    def getFileName(self):
        filename = input('Enter a filename: ')
        return filename

    def readFromStandardFile(self):
        filename = self.getFileName()

    def startApp(self):
        listOfCommands = {
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
        }
        while True:
            self.showMenu()
            command = self.getCommand()
            if command == 9:
                print('You\'ve left the app!')
                break
            listOfCommands[command]()
