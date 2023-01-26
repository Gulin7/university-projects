import os

from src.domain.Expense import Expense
from src.infrastructure.MemoryRepo import MemoryRepo


class TextFileRepo(MemoryRepo):
    """
        TEXTFILE_REPO C.R.U.D. OPERATIONS
    """

    def __init__(self, file_name):
        # super().__init__()
        MemoryRepo.__init__(self)
        self.__file_name = file_name
        self.__read_file_data_to_expenses_list()

    def get_file(self):
        return self.__file_name

    def set_file(self, file_name):
        self.__file_name = file_name

    def __read_file_data_to_expenses_list(self):
        if os.path.getsize(self.__file_name) <= 0:
            self._repo = []
            return
        with open(self.__file_name, "r") as f:
            f.seek(0)
            file_lines = f.read().strip().split('\n')
        for line in file_lines:
            expenses_details = line.split(',')
            try:
                expense = Expense(int(expenses_details[0]), int(expenses_details[1]), expenses_details[2])
                self._repo.append(expense)
            except:
                pass
        f.close()

    def __write_expenses_to_file(self):
        with open(self.__file_name, "w") as file:
            for expense in self._repo:
                file.write(
                    str(expense.get_day()) + ", " + str(expense.get_amount()) + ", " + str(expense.get_type()) + "\n")
        file.close()

    def __append_expenses_to_file(self, expense: Expense):
        with open(self.__file_name, "a") as file:
            file.write(
                str(expense.get_day()) + ", " + str(expense.get_amount()) + ", " + str(expense.get_type()) + "\n")
        file.close()

    def add_expense_to_repo(self, expense: Expense):
        MemoryRepo.add_expense_to_repo(self, expense)
        self.__append_expenses_to_file(expense)

    def get_all_expenses(self):
        # self.__read_file_data_to_expenses_list()
        return MemoryRepo.get_all_expenses(self)

    def set_expenses(self, new_list_of_expenses):
        MemoryRepo.set_expenses(self, new_list_of_expenses)
        self.__write_expenses_to_file()
