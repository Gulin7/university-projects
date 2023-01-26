import prettytable
from prettytable import PrettyTable

from src.service.service import Service


class Ui:
    def __init__(self, service: Service):
        self.__service = service

    def show_board(self):
        # print(self.__service.get_board())
        table = PrettyTable()
        table.hrules = prettytable.ALL
        table.header = False
        for row in self.__service.get_board():
            # print(row)
            new_row = []
            for i in row:
                # print(i)
                if i == 0:
                    new_row.append('')
                else:
                    new_row.append('x')
            table.add_row(new_row)
        print(table)

    def get_command(self):
        while True:
            try:
                command = input('Enter a command: ').lower().strip().split(' ')
                return command
            except ValueError as ve:
                print('Invalid command!', ve)

    def do_tick(self):
        self.__service.do_tick()

    def do_tick_n(self, n):
        for i in range(n):
            self.__service.do_tick()

    def start_console(self):
        self.show_board()
        commands = ['tick', 'save', 'load', 'exit', 'place', 'show', 'clear']
        patterns = ['block', 'blinker', 'tub', 'beacon', 'spaceship']
        while True:
            try:
                command = self.get_command()
                if command[0] not in commands:
                    raise ValueError('Not a good command :P 😢😭')
                # print(command)
                if len(command) == 1:
                    command = command[0]
                    if command == 'clear':
                        board = [[0 for i in range(8)] for i in range(8)]
                        self.__service.set_board(board)
                    elif command == 'exit':  # EXIT
                        print('You left the game! 😒👿')
                        return
                    elif command == 'tick':  # TICK NORMAL
                        self.do_tick()
                    elif command == 'show':  # SHOW
                        self.show_board()
                    else:
                        raise ValueError('Invalid command! 👎👺')
                elif len(command) == 2:
                    if command[0] == 'tick':  # TICK N
                        self.do_tick_n(int(command[1]))
                    elif command[0] == 'save':  # SAVE
                        self.__service.set_file(command[1])
                        self.__service.get_repo().write_to_file()
                    elif command[0] == 'load':  # LOAD
                        self.__service.set_file(command[1])
                        self.__service.get_repo().read_from_file()
                    else:
                        raise ValueError('Invalid command! 👎👺😢')
                elif len(command) == 3:
                    if command[0] != 'place':
                        raise ValueError('Invalid command! 😖')
                    else:
                        shape = command[1]
                        if shape not in patterns:
                            raise ValueError('Invalid pattern! 💩')
                        else:
                            coordinates = command[2].split(',')
                            self.__service.add_pattern(shape, int(coordinates[0]), int(coordinates[1]))
                else:
                    raise ValueError('Invalid command! 😭😒😖')
            except Exception as e:
                print('Invalid command!', e)
