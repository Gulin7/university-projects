from controller.controller import Controller


class Ui:
    def __init__(self, controller: Controller):
        self.__controller = controller

    @staticmethod
    def show_menu():
        print("""   HANGMAN
1. Add a new sentence
2. Start the game
3. Exit""")

    def get_command(self):
        while True:
            try:
                command = int(input('Enter a command: '))
                if 0 < command < 4:
                    return command
                else:
                    print('Invalid command!')
            except ValueError as ve:
                print('Invalid command!', ve)

    def add_sentence(self):
        while True:
            sentence = input('Enter a sentence: ')
            if self.__controller.check_validity(sentence):
                self.__controller.add_sentence(sentence)
                break
            else:
                print('Invalid sentence!')
        return

    def run_game(self):
        pass

    def start(self):
        while True:
            self.show_menu()
            command = self.get_command()
            if command == 3:
                print('You\'ve left the app! :(')
                return
            elif command == 2:
                self.run_game()
                return
            else:
                self.add_sentence()
            try:
                if command == 3:
                    print('You\'ve left the app! :(')
                    return
                elif command == 2:
                    self.run_game()
                    return
                else:
                    self.add_sentence()
            except ValueError as ve:
                print(ve)
