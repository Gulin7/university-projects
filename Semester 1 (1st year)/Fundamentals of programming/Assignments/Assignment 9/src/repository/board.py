import copy

from src.domain.constants import COLUMNS, ROWS


class Board:
    def __init__(self):
        self.__board = [[0 for i in range(COLUMNS)] for j in range(ROWS)]

    def get_board(self):
        """
        Gets the board.

        :return: board as matrix
        """
        return self.__board

    def set_board(self, board):
        """
        Sets the board.

        :param board:
        :return:
        """
        self.__board = board

    def add_piece(self, column, player):
        """

        :param column: the column we want to add a piece to
        :param player: the player who adds the piece
        :return: none
        """
        if column > 7 or column < 0:
            return
        for row in range(ROWS - 1, -1, -1):
            if self.__board[row][column] == 0:
                self.__board[row][column] = player
                return
