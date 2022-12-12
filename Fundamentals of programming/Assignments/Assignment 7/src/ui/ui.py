from prettytable import PrettyTable as pt
import copy


class Ui:
    def __init__(self, service):
        self.__service = service
        self.__commands = {"add": self.__service.add_expenses_to_service,
                           "display": self.print_service,
                           "filter": self.__service.filter_expenses}

    def print_menu(self):
        print("""   OPTIONS MENU:
>>>Add
>>>Display
>>>Filter
>>>Undo
>>>Exit
-----------------------------------""")

    def read_command(self):
        command = input("Enter a command: ")
        command = command.lower()
        pos = command.find(" ")
        if pos == -1:
            return command, []
        cmd = command[:pos]
        args = command[pos + 1:]
        args = args.split(',')
        args = [s.strip() for s in args]
        args = args[0].split(' ')
        return cmd, args

    def print_service(self):
        table = pt()
        table.field_names = ["EXPENSES", "DAY", "AMOUNT", "TYPE"]
        display = copy.deepcopy(self.__service.get_all_expenses_in_service())
        index = 1
        for expense in display:
            ok = 1
            try:
                table.add_row(
                    [f'Expense {index}', str(expense['day']), str(expense['amount']), str(expense['type'])])
                ok = 0
            except:
                pass
            if ok == 1:
                table.add_row(
                    [f'Expense {index}', str(expense.get_day()), str(expense.get_amount()), str(expense.get_type())])
            index += 1
        print(table)

    def start_ui(self):
        while True:
            # print(self.__service.history)
            # print(self.__service.get_all_expenses_in_service())
            self.print_menu()
            cmd, args = self.read_command()
            if cmd == "exit":
                print("You've left the app! Goodbye... 👋😢😭")
                break
            elif cmd == "undo":
                try:
                    self.__service.undo()
                except ValueError as ve:
                    print(ve)
            else:
                self.__commands[cmd](*args)
                try:
                    # self.__commands[cmd](*args)
                    pass
                except TypeError as te:
                    print('Invalid command! 👎', te)
                except KeyError as ke:
                    print('Invalid command! 👎', ke)
                except ValueError as ve:
                    print('Invalid command! 👎', ve)
                except AttributeError as ae:
                    print('Invalid command! 👎', ae)
                except:
                    print('Invalid command! 👎')
