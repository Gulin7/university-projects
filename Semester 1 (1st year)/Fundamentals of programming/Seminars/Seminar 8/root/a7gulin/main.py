from root.a7gulin.domain.entities import Expense
from root.a7gulin.repository.expenses_repository import ExpenseRepository
from root.a7gulin.service.expenses_service import ExpenseService


def main():
    expense = Expense(1, 14, 300, 'groceries')
    expense_repo = ExpenseRepository()
    expense_service = ExpenseService(expense_repo)
    

if __name__ == '__main__':
    main()
