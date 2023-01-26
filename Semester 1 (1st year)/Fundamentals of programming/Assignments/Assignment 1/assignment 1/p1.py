# Solve the problem from the first set here
from math import sqrt


def is_prime(n):
    """
    This function checks if a number is prime or not.

    We return 1 if the given number is 2 and 0 if it's lower than 2 ore higher and even.
    We then check if the number has any odd divisors and return 0 if it does.
    :param n: the number we check
    :return: 1 if its prime
    """
    if n == 2:
        return 1
    if n < 2 or n % 2 == 0:
        return 0
    stop = int(sqrt(n)) + 1
    for div in range(3, stop, 2):
        if n % div == 0: return 0


if __name__ == '__main__':
    n = int(input("Your chosen number is: "))
    prime = n + 1
    while is_prime(prime) == 0:
        prime += 1
    print(f"The first prime number larger than {n} is {prime}")
