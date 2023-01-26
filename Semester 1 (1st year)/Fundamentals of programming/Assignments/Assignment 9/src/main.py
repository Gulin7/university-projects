from src.repository.board import Board
from src.services.game_service import Game
from src.ui.ui import Ui


def main():
    board = Board()
    game = Game(board)
    ui = Ui(game)


if __name__ == '__main__':
    main()
