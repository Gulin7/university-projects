import copy

from src.domain.constants import ROWS, COLUMNS
from src.services.game_service import Game


class Ui:
    def __init__(self, game: Game):
        self.__game = game
        self.start_ui()

    @staticmethod
    def __display_menu():
        print("""           MENU
    Hello! 👋
    This is my game of Connect Four! The rules are simple: try to place your pieces on the following columns such that
you connect four of them, on one of the rows, columns or diagonals. Do that before the computer does and you win! Gl hf!

""")

    def __display_board(self):
        board = copy.deepcopy(self.__game.get_board())
        for row in range(ROWS):
            for column in range(COLUMNS):
                if board[row][column] == 0:
                    print('⚪', end=' ')
                elif board[row][column] == 1:
                    print(self.__player_color, end=' ')
                else:
                    print(self.__computer_color, end=' ')
            print('')

    def __pick_colors(self):
        colors = {'red': '🔴', 'orange': '🟠', 'yellow': '🟡', 'green': '🟢', 'blue': '🔵', 'purple': '🟣', 'brown': '🟤',
                  'black': '⚫'}
        print("""Available colors:
1. red
2. orange
3. yellow
4. green
5. blue
6. purple
7. brown
8. black
""")
        while True:
            player_color = input('Enter a player color: ').lower()
            computer_color = input('Enter a computer color: ').lower()
            if player_color and computer_color in colors.keys():
                if player_color != computer_color:
                    self.__player_color = colors[player_color]
                    self.__computer_color = colors[computer_color]
                    break
                else:
                    print('You cannot have the same color as the computer')
            else:
                print('Invalid colors!')

    def __get_column_from_user(self):
        while True:
            try:
                column = int(input('Enter a column between 1 and 7: '))
                if column < 1 or column > 7:
                    print('Invalid column!')
                else:
                    if self.__game.check_valid_column(column - 1):
                        return column - 1
                    else:
                        print('Invalid column!')
            except ValueError as ve:
                print('Invalid column!', ve)

    def start_ui(self):
        current_player = self.__game.get_player()
        self.__display_menu()
        self.__pick_colors()
        while True:
            self.__display_board()
            if self.__game.check_victory():
                if self.__game.get_player() == 2:
                    print('You win!!!')
                    break
                else:
                    print('Computer wins!')
                    break
            if not self.__game.check_remaining_moves():
                print('There are no moves left! It\'s a draw!')
                break
            if self.__game.get_player() == 1:
                print('The player moves: ')
                try:
                    column = self.__get_column_from_user()
                    self.__game.add_piece(column, self.__game.get_player())
                except:
                    pass
            else:
                print('The computer moves! ')
                self.__game.normal_ai_move()
            self.__game.change_player()
