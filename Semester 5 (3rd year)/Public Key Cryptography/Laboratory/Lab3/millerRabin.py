import random

def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def millerRabin(d, n):
    # pick a random base
    base = 2 + random.randint(1, n - 1)

    # compute base^d % n
    x = base ^ d % n

    # x is 1 or (n-1) => n prime (probably)
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = x ^ 2 % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

if __name__ == '__main__':
    pass