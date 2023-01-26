from root.services.functions import *


def base2_to_base4(number_in_base2):
    """
    RAPID CONVERT FROM BASE2 TO BASE4

    :param number_in_base2: number in base2
    :return: number in base4
    """
    rapid_convert = {'00': '0', '01': '1',
                     '10': '2', '11': '3', }
    number_base2_as_string = str(number_in_base2)
    while len(number_base2_as_string) % 2 != 0:
        number_base2_as_string = '0' + number_base2_as_string
    resulted_number = ''
    for index in range(0, len(number_base2_as_string) - 1, 2):
        resulted_number = resulted_number + str(rapid_convert[number_base2_as_string[index:index + 2]])
    return resulted_number


def base2_to_base8(number_in_base2):
    """
    RAPID CONVERT FROM BASE2 TO BASE8

    :param number_in_base2: number in base 2
    :return: number in base 8
    """
    rapid_convert = {'000': '0', '001': '1',
                     '010': '2', '011': '3',
                     '100': '4', '101': '5',
                     '110': '6', '111': '7', }
    resulted_number = ''
    number_base2_as_string = convert_list_number_to_string(convert_number_to_list(number_in_base2))
    while len(number_base2_as_string) % 3 != 0:
        number_base2_as_string = '0' + number_base2_as_string
    for index in range(0, len(number_base2_as_string) - 2, 3):
        resulted_number = resulted_number + str(rapid_convert[number_base2_as_string[index:index + 3]])
    return resulted_number


def base2_to_base16(number_in_base2):
    """
    RAPID CONVERT FROM BASE2 TO BASE16

    :param number_in_base2: number in base2
    :return: number in base8
    """
    rapid_convert = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                     '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                     '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                     '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F', }
    resulted_number = ''
    number_base2_as_string = str(number_in_base2)
    while len(number_base2_as_string) % 4 != 0:
        number_base2_as_string = '0' + number_base2_as_string
    for index in range(0, len(number_base2_as_string) - 3, 4):
        resulted_number = resulted_number + str(rapid_convert[str(number_base2_as_string[index:index + 4])])
    return resulted_number


def rapid_convert_from_base2_to_given_base(number_in_base2, given_base):
    """
    Rapid convert a number in base2 to a given base, that can be 4, 8 or 16

    :param number_in_base2:
    :param given_base:
    :return:
    """
    if given_base == 4:
        return base2_to_base4(number_in_base2)
    elif given_base == 8:
        return base2_to_base8(number_in_base2)
    elif given_base == 16:
        return base2_to_base16(number_in_base2)
    return '0'


def rapid_convert_to_base2_from_given_base(number, given_base):
    """
    Converts a number to base 2, using rapid conversions.

    :param number: int, given number
    :param given_base: int, given base
    :return: the given number converted to base 2
    """
    if given_base == 2:  # if the number is already in base 2 then we just return it
        return convert_list_number_to_string(convert_number_to_list(number))
    # we create a dictionary for each rapid conversion
    base16_to_base2 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                       '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                       '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
                       'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111', }
    base8_to_base2 = {'0': '000', '1': '001', '2': '010', '3': '011',
                      '4': '100', '5': '101', '6': '110', '7': '111', }
    base4_to_base2 = {'0': '00', '1': '01', '2': '10', '3': '11', }
    # we get the number as string using the 2 functions we have
    number_as_string = convert_list_number_to_string(convert_number_to_list(number))
    number_in_base2 = ''
    if given_base == 4:
        for index in range(len(number_as_string)):
            number_in_base2 = number_in_base2 + str(base4_to_base2[number_as_string[index]])
    elif given_base == 8:
        for index in range(len(number_as_string)):
            number_in_base2 = number_in_base2 + str(base8_to_base2[number_as_string[index]])
    elif given_base == 16:
        for index in range(len(number_as_string)):
            number_in_base2 = number_in_base2 + str(base16_to_base2[number_as_string[index]])
    #print(number_in_base2)
    return number_in_base2
