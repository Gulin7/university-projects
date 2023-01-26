from src.domain.expenses import Expenses
from src.infrastructure.expenses_repository import ExpensesRepo


class ExpensesFileRepository(ExpensesRepo):
    def __init__(self, file_name):
        super().__init__()  # super class call
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                array = line.split(',')
                # TODO: try and except to validate the array input
                expense = Expenses(array[0], array[1], array[2])
                super().add_expenses_to_repo(expense)  # after validation
