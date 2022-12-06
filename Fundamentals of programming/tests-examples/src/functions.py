import random


def generate_random_secret_number():
    """
    Generates a random 4 digits number, with all digits being different.

    :return: int, 4 digit number, all digits different
    """
    a = random.randint(1, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    while not check_number_rule_1(a * 1000 + b * 100 + c * 10 + d):
        a = random.randint(1, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
    return a * 1000 + b * 100 + c * 10 + d


def check_number_rule_1(x):
    """
    Checks a number to see if it is ok based on the rule 1.

    :param x: int
    :return: True/False, depending if the number corresponds to the rule1 or not
    """
    if x < 1023 or x > 9876:
        return False
    a = x % 10
    x = x // 10
    b = x % 10
    x = x // 10
    c = x % 10
    x = x // 10
    d = x % 10
    if a != b and a != c and a != d and b != c and b != d and c != d:
        return True
    return False
