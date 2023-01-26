from src.domain.Expense import *


class MemoryRepo:
    """
        MEMORY_REPO C.R.U.D. OPERATIONS
    """

    def __init__(self):
        """ LIST OF ALL EXPENSES"""
        self._repo = list()

    def add_expense_to_repo(self, expense):
        """
        Adds a new expense to the _repo.
        :param expense: Expense
        :return: updates the _repo
        """
        if expense in self._repo:
            raise ValueError("existing entity!")
        self._repo.append(expense)

    def number_of_expenses(self):
        """

        :return: int, the number of expenses in the _repo
        """
        return len(self._repo)

    def get_all_expenses(self):
        """

        :return: the _repo itself(list of Expense)
        """
        return list(self._repo)

    def search_expense_in_repo(self, expense):
        """
        Searches for an expense in the repository.
        :param expense:
        :return:
        """
        repo_aux = self.get_all_expenses()
        for _expense in repo_aux:
            if _expense.equal_expenses(expense):
                return _expense
        raise ValueError('expense not found!')

    def set_expenses(self, new_list):
        """
        Updates the repository to a new one.
        :param new_list: a list of expenses
        :return: none, updates the _repo
        """
        self._repo = list(new_list)

    def remove_expense(self, expense):
        """
        Deletes an expense from the _repo
        :param expense: Expense
        :return: none, updates the _repo
        """
        if expense not in self._repo:
            raise ValueError("inexisting entity!")
        self._repo.remove(expense)

