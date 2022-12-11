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
        remainder = float(number) - int(number)
        number = int(number)
        while number > 0:
            number_base10 += number % 10 * power
            power *= base
            number = number // 10
        remainder_result = 0
        power = 1 / base
        while remainder != 0:
            remainder = remainder * 10
            number += int(remainder) * power
            power = power / base
            remainder = remainder - int(remainder)
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
    number_base10 = float(number_base10)
    remainder = float(number_base10) - int(number_base10)
    remainder_base16 = remainder
    number_base10 = int(number_base10)
    number = 0
    power = 1
    negative = 0
    if number_base10 < 0:  # we check if the number is negative
        negative = 1
        number_base10 = -number_base10
    if base != 16:  # we create a number with each remainder
        while number_base10 > 0:
            number += (number_base10 % base) * power
            power *= 10
            number_base10 = number_base10 // base

        power = 1 / 10
        for i in range(5):
            remainder = remainder * base
            number += int(remainder) * power
            power = power / 10
            remainder = remainder - int(remainder)
            if remainder == 0:
                break
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
        number = number + '.'
        for i in range(5):
            remainder_base16 = remainder_base16 * base
            if int(remainder_base16) >= 10:
                print(int(remainder_base16))
                number += remainders[int(remainder_base16)]
            else:
                number += str(int(remainder_base16))
            remainder_base16 = remainder_base16 - int(remainder_base16)
            if remainder_base16 == 0:
                break
    if negative == 1:
        return -number
    return number
