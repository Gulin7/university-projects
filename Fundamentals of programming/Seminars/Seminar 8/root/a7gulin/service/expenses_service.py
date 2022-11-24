from root.a7gulin.domain.entities import Expense


class ExpenseService:
    def __init__(self, expense_repo):
        self.__expense_repo = expense_repo

    def add_expense(self, expense_id, day, amount, type):
        expense = Expense(expense_id, day, amount, type)
        self.__expense_repo.save(expense)

    def list_all_expenses(self):
        return self.__expense_repo.find_all()
