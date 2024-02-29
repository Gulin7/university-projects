class Item:

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received args
        assert price > 0, f"Price: {price} is not greater than zero!"
        assert quantity > 0, f"Quantity: {quantity} is not greater than zero!"
        # Assign to self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_name(self, new_name):
        self.__name = new_name

    def set_price(self, new_price):
        self.__price = new_price

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity
