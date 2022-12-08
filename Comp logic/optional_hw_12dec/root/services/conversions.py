def convert_to_base10(number, base):
    """
    Converts a number into base 10.

    :param number: given number, int (or string for base16)
    :param base: given base, int
    :return: int, number in base 10
    """
    number_base10 = 0
    power = 1
    if base != 16:
        number = int(number)
        while number > 0:
            number_base10 += number % 10 * power
            power *= base
            number = number // 10
    else:
        digits_base_16 = {'1': 1, '2': 2, '3': 3, '4': 4,
                          '5': 5, '6': 6, '7': 7, '8': 8,
                          '9': 9, 'A': 10, 'B': 11, 'C': 12,
                          'D': 13, 'E': 14, 'F': 15, }
        for index_digit in reversed(number):
            digit = index_digit.upper()
            number_base10 += digits_base_16[digit] * power
            power *= 16
    return number_base10


def convert_from_base10_to_base(number_base10, base):
    """
    Converts a number from base 10 to a given base.

    :param number_base10: int, number in base10
    :param base: the base we are converting into
    :return: the converted number
    """
    number_base10 = int(number_base10)
    number = 0
    power = 1
    negative = 0
    if number_base10 < 0: # we check if the number is negative
        negative = 1
        number_base10 = -number_base10
    if base != 16: # we create a number with each remainder
        while number_base10 > 0:
            number += (number_base10 % base) * power
            power *= 10
            number_base10 = number_base10 // base
    else:
        number = ''
        remainders = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while number_base10 > 0:
            remainder = number_base10 % 16
            if remainder > 9:
                number = remainders[remainder] + number
            else:
                number = str(remainder) + number
            number_base10 = number_base10 // 16
    if negative == 1:
        return -number
    return number
