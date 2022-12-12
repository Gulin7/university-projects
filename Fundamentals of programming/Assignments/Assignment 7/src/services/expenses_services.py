import copy
import random

from src.infrastructure.MemoryRepo import *
from src.domain.Expense import *


class ExpensesService:

    def __init__(self, expenses_repo):
        self._repo = expenses_repo
        self.history = []

    def add_expenses_to_service(self, day, amount, type):
        self.update_history()
        expense = Expense(day, amount, type)
        repo = self._repo.get_all_expenses()
        for _expense in repo:
            # print(_expense)
            if _expense.equal_expenses(expense):
                raise ValueError("existing expense!")
        self._repo.add_expense_to_repo(expense)

    def get_all_expenses_in_service(self):
        return self._repo.get_all_expenses()

    def no_of_expenses_in_service(self):
        return self._repo.number_of_expenses()

    def remove_expense_service(self, expense: Expense):
        self._repo.remove_expense(expense)

    def filter_expenses(self, amount: int):
        self.update_history()
        to_remove = []
        for expense in self._repo.get_all_expenses():
            if int(expense.get_amount()) <= int(amount):
                to_remove.append(expense)
        for expense in to_remove:
            self.remove_expense_service(expense)

    def generate_random_expenses(self):
        list_of_expenses_types = ['Food', 'Clothes', 'Jewelry', 'Rent', 'Taxes', 'Gas',
                                  'Mortgage', 'Cinema', 'Groceries', 'VideoGames', 'OnlineShopping', 'Gifts',
                                  'Insurance']
        for index in range(10):
            self._repo.add_expense_to_repo(
                Expense(random.randint(1, 30), random.randint(1, 1000), random.choice(list_of_expenses_types)))

    def update_history(self):
        new_list = list(self._repo.get_all_expenses())
        self.history.append(copy.deepcopy(new_list))

    def undo(self):
        if len(self.history) == 0:
            raise ValueError('nothing to undo!')
        self._repo.set_expenses(self.history.pop())
