import copy

from src.exceptions.exceptions import BadCoordinates, BadPattern
from src.service.service import Service
from src.repository.Repository import Repository
import unittest


class TestFunctionality3(unittest.TestCase):
    def test__ok(self):
        repo = Repository()
        service = Service(repo)
        auxiliary_board = [[0 for i in range(8)] for i in range(8)]
        self.assertEqual(auxiliary_board, repo.get_board())
        self.assertEqual(auxiliary_board, service.get_board())
        auxiliary_board = [[i for i in range(8)] for i in range(8)]
        service.set_board(auxiliary_board)
        self.assertEqual(auxiliary_board, repo.get_board())
        self.assertEqual(auxiliary_board, service.get_board())

    def test_tick_1(self):
        """
        Tests tick for block.

        :return:
        """
        repo = Repository()
        service = Service(repo)
        service.add_pattern('block', 2, 2)
        auxiliary_board = copy.deepcopy(service.get_board())
        service.do_tick()
        self.assertEqual(auxiliary_board, service.get_board())
        for i in range(100):
            service.do_tick()
        self.assertEqual(auxiliary_board, service.get_board())

    def test_tick_2(self):
        """
        Tests tick for tub.

        :return:
        """
        repo = Repository()
        service = Service(repo)
        service.add_pattern('tub', 3, 3)
        auxiliary_board = copy.deepcopy(service.get_board())
        service.do_tick()
        self.assertEqual(auxiliary_board, service.get_board())
        for i in range(100):
            service.do_tick()
        self.assertEqual(auxiliary_board, service.get_board())

    def test_place(self):
        """
        Tests if the service.add_pattern works properly. With custom exceptions.

        :return:
        """
        repo = Repository()
        service = Service(repo)
        self.assertRaises(BadCoordinates, service.add_pattern, 'block', 7, 7)
        self.assertRaises(BadCoordinates, service.add_pattern, 'tub', 7, 7)
        self.assertRaises(BadCoordinates, service.add_pattern, 'spaceship', 7, 7)
        self.assertRaises(BadCoordinates, service.add_pattern, 'blinker', 7, 7)
        self.assertRaises(BadCoordinates, service.add_pattern, 'beacon', 7, 7)
        self.assertRaises(BadPattern, service.add_pattern, 'wroaaaaaa', 3, 3)

        # test block place
        service.add_pattern('block', 0, 0)
        self.assertEqual(service.get_board()[0][0], 1)
        self.assertEqual(service.get_board()[1][0], 1)
        self.assertEqual(service.get_board()[0][1], 1)
        self.assertEqual(service.get_board()[1][1], 1)

        # test tub place
        repo = Repository()
        service = Service(repo)
        service.add_pattern('tub', 0, 0)
        self.assertEqual(service.get_board()[0][1], 1)
        self.assertEqual(service.get_board()[1][2], 1)
        self.assertEqual(service.get_board()[2][1], 1)
        self.assertEqual(service.get_board()[1][0], 1)

    def test_check_neighbors(self):
        """
        Tests if the check_n works correctly ( if it calculates the correct number of neighbors).
        Teoretically this is enough to see if the tick functionality works properly.

        :return:
        """
        repo = Repository()
        service = Service(repo)
        board = service.get_board()
        board[2][3] = 1
        board[3][2] = 1
        board[4][5] = 1
        board[4][6] = 1
        board[4][7] = 1
        self.assertEqual(service.check_n(2, 3), 1)
        self.assertEqual(service.check_n(3, 2), 1)
        self.assertEqual(service.check_n(4, 5), 1)
        self.assertEqual(service.check_n(4, 6), 2)
        self.assertEqual(service.check_n(4, 7), 1)
