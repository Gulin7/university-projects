class Repository:
    def __init__(self):
        self.__board = [[0 for i in range(8)] for i in range(8)]

    def get_board(self):
        return self.__board

    def set_board(self, board):
        self.__board = board

