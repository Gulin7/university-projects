import copy
import json
import os

from src.domain.Expense import Expense
from src.infrastructure.MemoryRepo import MemoryRepo


class JsonRepo(MemoryRepo):
    """
        JSON_REPO C.R.U.D. OPERATIONS
    """

    def __init__(self, file_name):
        MemoryRepo.__init__(self)
        self.__file_name = file_name
        self.__read_expenses_json()

    def get_file(self):
        return self.__file_name

    def set_file(self, file_name):
        self.__file_name = file_name

    def get_expenses_json(self, new_list_of_expenses):
        expenses_json = []
        expenses_list = copy.deepcopy(new_list_of_expenses)
        for expense in list(expenses_list):
            expenses_json.append(expense.to_dict())
        return expenses_json

    def __read_expenses_json(self):
        if os.path.getsize(self.__file_name) <= 0:
            self._repo = []
            return
        with open(self.__file_name) as file:
            json_string = file.read()
        expenses_json_dict = json.loads(json_string)
        expenses_json_list = list(expenses_json_dict.values())
        # print(expenses_json_list)
        for index in range(len(expenses_json_list)):
            new_expense = Expense(expenses_json_list[index]['day'], expenses_json_list[index]['amount'],
                                  expenses_json_list[index]['type'])
            self._repo.append(new_expense)
        file.close()

    def __update_json_file(self, new_list_of_expenses):
        expenses_list = self.get_expenses_json(new_list_of_expenses)
        write_to_json = json.dumps(expenses_list)
        with open(self.__file_name, "w") as file:
            file.write(write_to_json)
        file.close()

    def add_expense_to_repo(self, expense: Expense):
        # self.__read_expenses_json()
        MemoryRepo.add_expense_to_repo(self, expense)
        self.__update_json_file(self._repo)

    def get_all_expenses(self):
        # self.__read_expenses_json()
        return MemoryRepo.get_all_expenses(self)

    def set_expenses(self, new_list_of_expenses):
        MemoryRepo.set_expenses(self, new_list_of_expenses)
        self.__update_json_file(self._repo)
