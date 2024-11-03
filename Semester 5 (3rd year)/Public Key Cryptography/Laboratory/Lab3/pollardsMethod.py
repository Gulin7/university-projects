def gcd(first, second):
    if (first == 0):
        return second
    if (second == 0):
        return first

    while second!=0:
        first, second = second, first % second
    return first

def func(x):
    return x**2 + 1

def funcModN(x, n):
    return func(x) % n

def pollardMethod(x0, n):
    d = 1
    xi = x2i = x0
    count = 0
    i = 0
    while (d == 1 or d == n) and count <= 1000:
        xi = funcModN(xi, n)
        x2i = funcModN(funcModN(x2i, n), n)
        i += 2
        d = gcd(abs(xi - x2i), n)
        count += 1

    print("n = " + str(d) + " * " + str(n // d))

if __name__ == '__main__':
    x0 = int(input("Enter x0: "))
    n = 2 ** 881 - 1
    pollardMethod(x0, n)