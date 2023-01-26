import copy
import random

from src.domain.constants import ROWS, COLUMNS
from src.repository.board import Board


class Game:
    def __init__(self, board: Board):
        self.__board = board
        self.__player = random.randint(1, 2)
        # the player is random: 1 for user, 2 for computer

    def get_board(self):
        return self.__board.get_board()

    def set_board(self, board: Board):
        self.__board = board

    def get_player(self):
        return self.__player

    def set_player(self, player):
        self.__player = player

    def change_player(self):
        """
        Changes the current player.

        :return:
        """
        if self.__player == 1:
            self.__player = 2
        else:
            self.__player = 1

    def check_valid_column(self, column):
        """
        Checks if the column is valid.

        :param column: column
        :return: bool
        """
        board = copy.deepcopy(self.__board.get_board())
        if board[0][column] != 0:
            return False
        return True

    def add_piece(self, column, player):
        """
        Adds a piece
        :param column: column
        :param player: 1 for player, 2 for comp
        :return: none
        """
        self.__board.add_piece(column, player)

    def check_victory(self):
        """
        Checks if someone won the game.

        :return: True if someone won, false if not
        """
        board = copy.deepcopy(self.__board.get_board())
        for row in range(ROWS):
            for column in range(COLUMNS - 3):
                try:
                    if board[row][column] == 0:
                        pass
                    elif board[row][column] == board[row][column + 1] and \
                            board[row][column] == board[row][column + 2] and \
                            board[row][column] == board[row][column + 3]:
                        return True
                except:
                    pass
        for column in range(COLUMNS):
            for row in range(ROWS - 3):
                try:
                    if board[row][column] == 0:
                        pass
                    elif board[row][column] == board[row + 1][column] and \
                            board[row][column] == board[row + 2][column] and \
                            board[row][column] == board[row + 3][column]:
                        return True
                except:
                    pass
        for row in range(ROWS - 3):
            for column in range(COLUMNS - 3):
                try:
                    if board[row][column] == 0:
                        pass
                    elif board[row][column] == board[row + 1][column + 1] and \
                            board[row][column] == board[row + 2][column + 2] and \
                            board[row][column] == board[row + 3][column + 3]:
                        return True
                except:
                    pass
        for row in range(3, ROWS):
            for column in range(COLUMNS - 3):
                try:
                    if board[row][column] == 0:
                        pass
                    elif board[row][column].color == board[row - 1][column + 1].color and \
                            board[row][column].color == board[row - 2][column + 2].color and \
                            board[row][column].color == board[row - 3][column + 3].color:
                        return True
                except:
                    pass
        return False

    def check_remaining_moves(self):
        """

        :return: True if there are remaining moves, false if there aren't
        """
        board = copy.deepcopy(self.__board.get_board())
        for column in range(COLUMNS):
            if board[0][column] == 0:
                return True
        return False

    def normal_ai_move(self):
        """
        If the comp can win, it will win.
        If I can win, it will stop me.
        Random else.

        :return: none
        """
        # FIRST WE CHECK TO SEE IF WE CAN WIN:
        for column in range(COLUMNS):
            board = copy.deepcopy(self.__board.get_board())
            auxiliary_board = Board()
            auxiliary_board.set_board(board)
            auxiliary_game = Game(auxiliary_board)
            auxiliary_game.add_piece(column, 2)
            if auxiliary_game.check_victory():
                self.add_piece(column, 2)
                return
        # IF WE CANNOT WIN THEN WE BLOCK
        for column in range(COLUMNS):
            board = copy.deepcopy(self.__board.get_board())
            auxiliary_board = Board()
            auxiliary_board.set_board(board)
            auxiliary_game = Game(auxiliary_board)
            auxiliary_game.add_piece(column, 1)
            if auxiliary_game.check_victory():
                self.add_piece(column, 2)
                return
        # IF NO PLAYER CAN WIN WE PUT A RANDOM PIECE IN
        if self.check_remaining_moves():
            while True:
                column = random.randint(0, 6)
                if self.check_valid_column(column):
                    self.add_piece(column, 2)
                    return
