import mysql.connector

from src.domain.Expense import Expense
from src.infrastructure.MemoryRepo import MemoryRepo


class SqlRepository(MemoryRepo):

    def __init__(self):
        MemoryRepo.__init__(self)
        self.__read_list_of_expenses()

    def __read_list_of_expenses(self):
        database = mysql.connector.connect(host="localhost", user="root", password="Mamaluinacho232#",
                                           database="expenses_schema",
                                           port=3306)
        cursor = database.cursor()
        cursor.execute("SELECT * FROM `expenses`")
        expenses = cursor.fetchall()  # returns them as list of tuples
        for expense in expenses:
            expense_chars = list(expense)
            self._repo.append(Expense(expense_chars[0], expense_chars[1], expense_chars[2]))
        database.close()

    def __set_database(self, new_list_of_expenses):
        database = mysql.connector.connect(host="localhost", user="root", password="Mamaluinacho232#",
                                           database="expenses_schema",
                                           port=3306)
        cursor = database.cursor()
        cursor.execute("DELETE FROM expenses")
        for expense in list(new_list_of_expenses):
            cursor.execute("INSERT INTO expenses(`day`,`amount`,`type`) VALUES (%s, %s, %s)",
                           (expense.get_day(), expense.get_amount(), expense.get_type()))
        database.commit()
        database.close()

    def __add_to_database(self, expense: Expense):
        database = mysql.connector.connect(host="localhost", user="root", password="Mamaluinacho232#",
                                           database="expenses_schema",
                                           port=3306)
        cursor = database.cursor()
        cursor.execute("INSERT INTO expenses(`day`,`amount`,`type`) VALUES (%s, %s, %s)",
                       (expense.get_day(), expense.get_amount(), expense.get_type()))
        database.commit()
        database.close()

    def __remove_from_database(self, expense: Expense):
        database = mysql.connector.connect(host="localhost", user="root", password="Mamaluinacho232#",
                                           database="expenses_schema",
                                           port=3306)
        cursor = database.cursor()
        cursor.execute("DELETE FROM expenses WHERE `day` = %s AND `amount` = %s AND `type` = %s",
                       [expense.get_day(), expense.get_amount(), expense.get_type()])
        database.commit()
        database.close()

    def add_expense_to_repo(self, expense: Expense):
        # create
        # self.__read_list_of_expenses()
        MemoryRepo.add_expense_to_repo(expense)
        self.__add_to_database(expense)

    def get_all_expenses(self):
        return MemoryRepo.get_all_expenses(self)

    def set_expenses(self, new_list_of_expenses):
        MemoryRepo.set_expenses(new_list_of_expenses)
        self.__set_database(self._repo)

    def remove_expense(self, expense: Expense):
        self.__read_list_of_expenses()
        MemoryRepo.remove_expense(self, expense)
        self.__remove_from_database(expense)
