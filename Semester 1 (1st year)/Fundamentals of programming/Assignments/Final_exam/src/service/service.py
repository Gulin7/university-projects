from src.exceptions.exceptions import BadCoordinates, BadPattern
from src.repository import TextFileRepository


class Service:
    def __init__(self, repository: TextFileRepository):
        self.__repo = repository

    def get_board(self):
        return self.__repo.get_board()

    def set_board(self, board):
        return self.__repo.set_board(board)

    def set_file(self, file_name):
        self.__repo.set_file(file_name)

    def get_repo(self):
        return self.__repo

    def add_pattern(self, shape, x, y):
        board = self.get_board()
        if shape == 'blinker':
            try:
                for i in range(y, y + 3):
                    if board[x][i] == 1:
                        raise ValueError('Overlap!')
                for i in range(y, y + 3):
                    board[x][i] = 1
            except IndexError as ie:
                raise BadCoordinates('Bad coordinates :p 🙈')
        elif shape == 'block':
            try:
                for i in range(y, y + 2):
                    if board[x][i] == 1:
                        raise ValueError('Overlap!')
                for i in range(x, x + 2):
                    if board[i][y] == 1:
                        raise ValueError('Overlap!')
                board[x][y] = 1
                board[x + 1][y] = 1
                board[x][y + 1] = 1
                board[x + 1][y + 1] = 1
            except IndexError as ie:
                raise BadCoordinates('Bad coordinates :p 🙈')
        elif shape == 'tub':
            try:
                if board[x][y + 1] == 1 or board[x + 1][y] == 1 or board[x + 1][y + 2] == 1 or board[x + 2][y + 1] == 1:
                    raise ValueError('Overlap!')
                else:
                    board[x][y + 1] = 1
                    board[x + 1][y] = 1
                    board[x + 1][y + 2] = 1
                    board[x + 2][y + 1] = 1
            except IndexError as ie:
                raise BadCoordinates('Bad coordinates :p 🙈')
        elif shape == 'beacon':
            self.add_pattern('block', x + 2, y + 2)
            self.add_pattern('block', x, y)
        elif shape == 'spaceship':
            try:
                if board[x][y + 1] == 1 or board[x + 1][y + 2] == 1 or board[x + 2][y] == 1 or board[x + 2][
                    y + 1] == 1 or \
                        board[x + 2][y + 2] == 1:
                    raise ValueError('They overlap! 👺')
                else:
                    board[x][y + 1] = 1
                    board[x + 1][y + 2] = 1
                    board[x + 2][y] = 1
                    board[x + 2][y + 1] = 1
                    board[x + 2][y + 2] = 1
            except IndexError as ie:
                raise BadCoordinates('Bad coordinates :p 🙈')
        else:
            raise BadPattern('Invalid pattern! so lame... 🙈🙈')
        self.set_board(board)

    def check_n(self, x, y):
        """
        Checks how many live neighbors are there for [x][y].

        :param x: the x coordinate
        :param y: the y coordinate
        :return: the number of alive neighbors for board[x][y]
        """
        neighbors = 0
        try:
            if self.get_board()[x][y - 1] == 1:
                neighbors = neighbors + 1
        except IndexError:
            pass
        try:
            if self.get_board()[x][y + 1] == 1:
                neighbors = neighbors + 1
        except IndexError:
            pass
        try:
            if self.get_board()[x - 1][y] == 1:
                neighbors = neighbors + 1
        except IndexError:
            pass
        try:
            if self.get_board()[x + 1][y] == 1:
                neighbors = neighbors + 1
        except IndexError:
            pass
        try:
            if self.get_board()[x - 1][y - 1] == 1:
                neighbors = neighbors + 1
        except IndexError:
            pass
        try:
            if self.get_board()[x + 1][y - 1] == 1:
                neighbors = neighbors + 1
        except IndexError:
            pass
        try:
            if self.get_board()[x - 1][y + 1] == 1:
                neighbors = neighbors + 1
        except IndexError:
            pass
        try:
            if self.get_board()[x + 1][y + 1] == 1:
                neighbors = neighbors + 1
        except IndexError:
            pass
        return neighbors

    def do_tick(self):
        """
        It performs a tick conform the 4 rules.
        It uses the function check_n to calculate how many LIVE neighbors the cell [i][j] has and depending on the resulted number,
        as well as if that cell is alive or not, it will change from 1 to 0.

        :return: none, sets the repository board to a new board, after exactly one tick
        """
        new_board = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                neighbors = self.check_n(i, j)
                if self.get_board()[i][j] == 0:
                    if neighbors == 3:
                        new_board[i][j] = 1
                elif self.get_board()[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
        self.set_board(new_board)
