from math import sqrt
import random
import copy
from ui import *

"""
    CREATES A NUMBER AS A LIST/DICT, MODIFY THE ORDER OR COMMENT 1 OUT TO WORK WITH THE DIFFERENT STRUCTURE
"""


def create_number(real_part, imaginary_part):
    """
    This function creates an imaginary number as a list.

    :param: real_part: float/int, the real part of an imaginary number
    :param: imaginary_part: float/int, the imaginary part of an imaginary number
    :return: an imaginary number as a list with the first element being the real part
    the second one being the imaginary part
    """
    complex_number = [real_part, imaginary_part]
    return complex_number


#def create_number(real_part, imaginary_part):
    """
        This function creates an imaginary number as a dictionary.

    :param: real_part: float/int, the real part of a complex number
    :param: imaginary_part: float/int, the imaginary part of a complex number
    :return: a dictionary with the keys real and imaginary
            representing the real/imaginary parts of a complex number
        """
    #complex_number = {'real': real_part, 'imag': imaginary_part}
    #return complex_number


def calculate_modulus(real_part, imaginary_part):
    """
    Calculates the modulus of a complex number

    :param real_part: float/int, real part of a complex number
    :param imaginary_part: float/int, imaginary part of a complex number
    :return: the modulus of a complex number
    """
    s = real_part * real_part + imaginary_part * imaginary_part
    if s == 0: return 0
    return sqrt(s)


"""
    GETS THE REAL & IMAGINARY PARTS OF A COMPLEX NUMBER REPRESENTED AS A LIST/DICT, CHANGE ORDER OR COMMENT ONE OUT
    TO SWITCH BETWEEN STRUCTURES
"""


def get_number(complex_list):
    """
    Returns the real and imaginary parts of a complex number, 2 separate variables.

    :param complex_list: list, containing the real and the imaginary parts of a complex number
    :return: the real part and the imaginary part of a complex number
    """
    return complex_list[0], complex_list[1]


#def get_number(complex_dict):
    """
    Returns the real and imaginary parts of a complex number, 2 separate variables.

    :param complex_dict: dictionary, containing the real and the imaginary parts of a complex number, with the keys:
    'real', respectively 'imag'
    :return: the real part and the imaginary part of a complex number
    """
    #return complex_dict['real'], complex_dict['imag']


"""
    RETURNS THE COMPLEX NUMBER, EITHER STORED AS A LIST OR A DICT, AS A STRING SUCH AS "a+bi"
"""


def to_string(num_list):
    """
    Prints the complex number "num" which is given as a list. "a+bi"

    :param: num_list: list/dict, 2 elements, first is the real part and 2nd is the imaginary part of a complex number
    :return: the complex number as a string
    """
    real_part, imaginary_part = get_number(num_list)
    if imaginary_part < 0:
        sign = "-"
        imaginary_part = -imaginary_part
    else:
        sign = "+"
    return str(str(real_part) + sign + str(imaginary_part) + "i")


"""
    GENERATES A LIST OF COMPLEX NUMBERS, EITHER AS LISTS OR AS DICTS; COMMENT OR CHANGE ORDER TO SWITCH STRUCTURES
"""


def generate_random_complex_number_list(length):
    """
    Generates a list of complex numbers.

    :param: length: the length of the list, integer
    :return: a list of "length" random generated complex numbers.
    """
    complex_set = list()
    for i in range(length):
        complex_set.append([random.randint(-100, 100), random.randint(-100, 100)])
    return complex_set


#def generate_random_complex_number_list(length):
    """
    Generates a list of complex numbers.

    :param: length: the length of the list, integer
    :return: a list of "length" random generated complex numbers.
    """
    #complex_set = list()
    #for i in range(length):
        #complex_set.append({'real': random.randint(-100, 100), 'imag': random.randint(-100, 100)})
    #return complex_set


"""
    SET PROBLEM B :P 
"""


# FIRST IMPLEMENTATION, NOT REALLY DYNAMIC PROGRAMMING
def longest_subarray_modulus(complex_set):
    """
    Computes the longest subarray of a given set of complex numbers, represented as either a list of dicts or
    a list of lists, with numbers that have modulus between 0 and 10.

    :param: complex_set: set of complex numbers
    :return: the longest subarray with elements with modules in range [0,10]
    """
    longest_subarray = list()
    maxim = 0
    current = 0
    current_subarray = list()
    for element in complex_set:
        real_part, imaginary_part = get_number(element)
        if 0 <= calculate_modulus(real_part, imaginary_part) <= 10:
            current += 1
            current_subarray.append(element)
        else:
            if current > maxim:
                maxim = current
                longest_subarray = copy.deepcopy(current_subarray)
            current = 0
            current_subarray = list()
    return longest_subarray


# 2nd implementation, using dynamic programming
def longest_subarray_modulus(complex_set):
    length = len(complex_set)
    maxim_length = -1
    maxim_length_position = 0
    check_complex_set = [0] * len(complex_set)
    real_part, imaginary_part = get_number(complex_set[0])
    if 0 <= calculate_modulus(real_part, imaginary_part) <= 10:
        check_complex_set[0] = 1
        maxim_length = 1
        maxim_length_position = 0
    for index in range(1, len(complex_set)):
        real_part, imaginary_part = get_number(complex_set[index])
        modulus = calculate_modulus(real_part, imaginary_part)
        if 0 <= modulus <= 10:
            check_complex_set[index] = check_complex_set[index - 1] + 1
            if maxim_length < check_complex_set[index]:
                maxim_length = check_complex_set[index]
                maxim_length_position = index
    longest_subarray = list()
    for index in range(maxim_length_position - maxim_length + 1, maxim_length_position + 1):
        longest_subarray.append(complex_set[index])
    return longest_subarray


"""
    SET PROBLEM A :O
"""


def check_increasing(my_list):
    """
    Checks if a list is strictly increasing or not.

    :param my_list: list, int
    :return: true if the list is strictly increasing
    """
    length = len(my_list)
    if length == 0:
        return 0
    for i in range(1, length):
        if my_list[i] < my_list[i - 1]:
            return 0
    return 1


def longest_increasing_modulus_subsequence(start, cur, curmod, complex_set, last):
    """
    This is a recursive backtracking algorithm that creates all the increasing subsequences of a complex set based on
    the number's modulus.

    :param: start: the index we start iterating from
    :param: cur: the current list of complex numbers
    :param curmod: the current list of modules of elements from cur
    :param complex_set: the initial set
    :param last: the final result set
    :return:
    """
    for i in range(start, len(complex_set)):
        real_part, imaginary_part = get_number(complex_set[i])
        curmod.append(calculate_modulus(real_part, imaginary_part))
        cur.append(to_string(complex_set[i]))
        if check_increasing(curmod):
            if len(curmod) > len(last):
                last = copy.deepcopy(cur)
            aux = longest_increasing_modulus_subsequence(i + 1, cur, curmod, complex_set, last)
            if len(aux) > len(last):
                last = copy.deepcopy(aux)
        cur.pop()
        curmod.pop()
    return last
