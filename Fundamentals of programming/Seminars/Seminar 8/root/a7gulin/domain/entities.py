"""
Expenses - day(1<->30), amount(>0, integer), type(string)
"""


class Expense:
    def __init__(self, expense_id, day, amount, type):
        # class attributes are hidden
        self.__expense_id = expense_id
        self.__day = day
        self.__amount = amount
        self.__type = type

    def get_id(self):
        return self.__expense_id

    def get_day(self):
        return self.__day

    def get_amount(self):
        return self.__amount

    def get_type(self):
        return self.__type

    def set_new_id(self, new_id):
        self.__expense_id = new_id

    def set_day(self, new_day):
        self.__day = new_day

    def set_amount(self, new_amount):
        self.__amount = new_amount

    def set_type(self, new_type):
        self.__type = new_type

    def __str__(self):
        return f"Expense: id = {self.__expense_id}, day = {self.__day}, amount = {self.__amount}, type = {self.__type}"
