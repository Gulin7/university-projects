class Console:
    def __init__(self, expenses_service):
        self.__expenses_service = expenses_service

    def run_console(self):
        self.__add_expenses()
        self.__print_all_expenses()

    def __add_expenses(self):
        self.__expenses_service.add_expenses(1, 12, 200, 'cinema')
        self.__expenses_service.add_expenses(2, 27, 5, 'milk')

    def __print_all_expenses(self):
        pass
