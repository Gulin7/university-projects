import copy
import os
import pickle

from src.domain.Expense import Expense
from src.infrastructure.MemoryRepo import MemoryRepo


class BinaryFileRepo(MemoryRepo):
    """
        BINARYFILE_REPO C.R.U.D. OPERATIONS
    """

    def __init__(self, file_name):
        MemoryRepo.__init__(self)
        self.__file_name = file_name
        self.read_expenses_from_binary_file()

    def get_file(self):
        return self.__file

    def set_file(self, file_name):
        self.__file = file_name

    def read_expenses_from_binary_file(self):
        if os.path.getsize(self.__file_name) <= 0:
            self._repo = []
            return
        with open(self.__file_name, 'rb') as file:
            self._repo = list(pickle.load(file))

    def write_expenses_to_binary_file(self):
        with open(self.__file_name, 'wb') as file:
            pickle.dump(self._repo, file)

    def add_expense_to_repo(self, expense: Expense):
        """
        Adds a new expense to the _repo.

        :param expense: Expense
        :return: none, updates the _repo and the binary file
        """
        MemoryRepo.add_expense_to_repo(self, expense)
        self.write_expenses_to_binary_file()

    def get_all_expenses(self):
        return MemoryRepo.get_all_expenses(self)

    def set_expenses(self, new_list_of_expenses):
        MemoryRepo.set_expenses(self, new_list_of_expenses)
        self.write_expenses_to_binary_file()

    def remove_expense(self, expense):
        MemoryRepo.remove_expense(self, expense)
        self.write_expenses_to_binary_file()
