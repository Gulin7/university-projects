def check_number_and_base(number, base):
    """
    Checks if a number is in base "base".

    :param number: the given number
    :param base: the given base
    :return: True if number is in base "base", false otherwise
    """
    try:
        copy = int(number)
    except:
        return False
    while copy > 0:
        digit = copy % 10
        if digit > 10:
            return False
        if digit >= base:
            return False
        copy = copy // 10
    return True


def check_number_base16(number):
    """
    Checks if a number is in base16.

    :param number: number in base 16
    :return: True if number is in base16, False otherwise
    """
    possible_base16_digits = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in number:
        if i.lower() not in possible_base16_digits:
            return False
    return True


def convert_number_to_list(number):
    """
    Creates a list of a numbers digits.

    :param number: given number
    :return: list, the number as a list
    """
    number_as_list = []
    if type(number) == int:
        while number > 0:
            number_as_list.append(number % 10)
            number = number // 10
    else:
        for index in range(len(number)):
            number_as_list.insert(0, number[index])
    return number_as_list


def convert_list_to_number_in_base(number_as_list, base):
    """
    Converts a number as a list to a number in base10
    :param number_as_list:
    :param base:
    :return:
    """
    number = 0
    power = 1
    for index in range(len(number_as_list)):
        number += number_as_list[index] * power
        power *= 10
    return number


def convert_list_to_number_in_base10(number_as_list, base):
    """
    Converts a number as a list to a number in base10
    :param number_as_list:
    :param base:
    :return:
    """
    number = 0
    power = 1
    for index in range(len(number_as_list)):
        number += number_as_list[index] * power
        power *= base
    return number


def create_dict_with_number_and_base(number, base):
    """
    Creates a dictionary of a number and it's base.

    :param number: given number
    :param base: given base
    :return: a dictionary with the number(as a list) and the base
    """
    dict_of_number_and_base = {'number': convert_number_to_list(number), 'base': base}
    return dict_of_number_and_base


def convert_list_number_to_string(number_as_list):
    """
    Converts a list representing a number to a string.

    :param number_as_list: list, representing a number
    :return: the number as a string
    """
    number_as_string = ''
    for index in range(len(number_as_list)):
        number_as_string = str(number_as_list[index]) + number_as_string
    return number_as_string
