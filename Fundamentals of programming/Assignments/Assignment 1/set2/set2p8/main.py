def fibonacci_f(n):
    """
    This function searches for the smallest bigger fibonacci number in raport to a given number(n).

    :param n: the given number
    :return: returns the smallest bigger than n fibonacci number
    """
    p1=1
    p2=1
    while p2<=n:
        copy=p2
        p2=p1+p2
        p1=copy
    return p2

if __name__ == '__main__':
    n=int(input("Your number is: "))
    print(f"The smallest number bigger than {n} that is part of the Fibonacci sequence is {fibonacci_f(n)}.")