import copy

from src.repository.board import Board
from src.services.game_service import Game
import unittest


class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        matrix = board.get_board()
        board.add_piece(3, 1)
        board.add_piece(3, 1)
        self.assertEqual(matrix[5][3], 1)
        self.assertEqual(matrix[4][3], 1)
        copied_matrix = copy.deepcopy(matrix)
        board.add_piece(9, 2)
        matrix = board.get_board()
        self.assertEqual(matrix, copied_matrix)


class TestGame(unittest.TestCase):
    def test_game(self):
        board = Board()
        game = Game(board)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        matrix = game.get_board()
        self.assertEqual(matrix[5][3], 1)
        self.assertEqual(matrix[4][3], 1)
        self.assertEqual(matrix[3][3], 1)
        self.assertEqual(matrix[2][3], 1)
        self.assertEqual(game.check_victory(), True)

    def test_ai(self):
        board = Board()
        game = Game(board)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        game.normal_ai_move()
        matrix = game.get_board()
        self.assertEqual(matrix[2][3], 2)

    def test_validator(self):
        board = Board()
        game = Game(board)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        game.add_piece(3, 1)
        self.assertEqual(game.check_valid_column(3), True)
        game.add_piece(3, 1)
        self.assertEqual(game.check_valid_column(3), False)

    def test_getters_setters_change_player(self):
        board = Board()
        game = Game(board)
        game.set_player(1)
        game.change_player()
        self.assertEqual(2, game.get_player())
        game.set_player(2)
        self.assertEqual(game.get_player(), 2)
        board2 = Board()
        game.set_board(board)
        self.assertEqual(game.get_board(), board2.get_board())
