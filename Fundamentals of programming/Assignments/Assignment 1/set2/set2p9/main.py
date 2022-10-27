def prod_of_proper_f(n):
    """
    This function computes the product of the parameters proper factors.

    :param n: the given number whose proper factor we are multiplying
    :return: the product of proper factors
    """
    p=1
    if n%2==0:
        while n%2==0: n=n/2
        p=p*2
    div=3
    while div<=n:
        if n%div==0:
            while n%div==0: n=n/div
            p=p*div
        div=div+2
    return p
if __name__ == '__main__':
    n=int(input("Input a number :) : "))
    print(f"The product of your number's proper factors is {prod_of_proper_f(n)}. :P")
