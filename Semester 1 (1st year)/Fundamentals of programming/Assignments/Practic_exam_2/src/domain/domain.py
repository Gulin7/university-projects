import math


class Address:
    def __init__(self, id, name, number, x, y):
        self.__id = id
        self.__name = name
        self.__number = number
        self.__x = x
        self.__y = y

    """
    GETTERS AND SETTERS
    """

    def get_id(self, ):
        return self.__id

    def get_name(self, ):
        return self.__name

    def get_number(self, ):
        return self.__number

    def get_x(self, ):
        return self.__x

    def get_y(self, ):
        return self.__y

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def equal_address(self, address):
        """
        Checks if 2 addresses are equal
        :param address: Address
        :return: bool
        """

        if self.get_name() == address.get_name() and self.get_y() == address.get_y() and self.get_x() == address.get_x() and self.get_id() == address.get_id() and self.get_number() == address.get_number():
            return True
        return False

    def get_distance_to_point(self, x, y):
        """
        Gets the distance from the address to a given point.

        :param x: x, int
        :param y: y, int
        :return: distance from the address to the point x,y
        """
        return math.sqrt(
            abs((self.get_x() - x)) * abs((self.get_x() - x)) + abs((self.get_y() - y)) * abs((self.get_y() - y)))

    def __str__(self):
        return str(
            f'Address: {self.get_id()}, {self.get_name()}, {self.get_number()}, {self.get_x()}, {self.get_y()}')
