class ExpenseRepository:
    def __init__(self):
        self.__all_expenses = {}

    def find_all(self):
        return list(self.__all_expenses.values())

    def __find_by_id(self, expense_id):
        if expense_id in self.__all_expenses:
            return self.__all_expenses[expense_id]

    def save(self, expense):
        if self.__find_by_id(expense.get_id()) is not None:
            raise ValueError("duplicate id")
        self.__all_expenses[expense.get_id()] = expense

    def update(self, expense_id, expense):
        if self.__find_by_id(expense_id) is None:
            raise ValueError("nonexisting id")
        self.__all_expenses[expense_id] = expense

    def delete_by_id(self, expense_id):
        if self.__find_by_id(expense_id) is None:
            raise ValueError("nonexisting id")
        del self.__all_expenses[expense_id]
