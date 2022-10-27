from math import sqrt
def is_prime(p):
    """
    This function checks if a given number is prime.

    :param p: the number whose primality is checked
    :return: 1 for prime, 0 contrary
    """
    if p==2:return 1
    if p<2 or p%2==0: return 0
    stop = int(sqrt(p)+1) # a variable used to mark where our for should end
    for div in range(3,stop,2):
        if p%div==0:return 0
    return 1

if __name__ == '__main__':
    n = int(input("Enter your number: "))
    lprime = n-1
    while is_prime(lprime)==0:
        lprime-=1
    print(f"The largest prime number smaller than {n} is {lprime}.")