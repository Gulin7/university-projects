class Expense:
    def __init__(self, day, amount, type):
        self.__day = day
        self.__amount = amount
        self.__type = type

    """
    GETTERS
    """

    def get_day(self):
        return self.__day

    def get_amount(self):
        return self.__amount

    def get_type(self):
        return self.__type

    """
    SETTERS
    """

    def set_day(self, new_day):
        self.__day = new_day

    def set_amount(self, new_amount):
        self.__amount = new_amount

    def set_type(self, new_type):
        self.__type = new_type

    def equal_expenses(self, expense):
        """
        Checks if 2 expenses are equal.
        :param expense: Expense
        :return: bool, True if the expense itself (self) is equal to the given parameter expense
        """
        return self.__day == expense.__day and self.__amount == expense.__amount and self.__type and expense.__type

    """
    __str__ FOR EXPENSES!
    """

    def __str__(self):
        return f"Day: {self.__day}, amount spent: {self.__amount}, for: {self.__type}."

    def to_dict(self):
        return {
            'day': self.get_day(),
            'amount': self.get_amount(),
            'type': self.get_type(),
        }
