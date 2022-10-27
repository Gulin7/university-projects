from math import sqrt
def is_prime(nr):
    """
    This functions checks if a number is prime or not.

    We take a given number nr and check if it is prime or not. The number 2 is prime so we return 1 and then we
    return 0 for any other even number and for 0 and 1(which are also not prime). The while is used to check whether or
    not does our number divide by any odd number smaller or equal to square root of itself. If it is divided by any that
    means it is not prime so we return 0.

    :param nr: the number whose primality we are checking
    :return: 0 if the number isn't prime and 1 if it is prime
    """
    if nr==2: return 1
    if nr<2 or nr%2==0: return 0
    div=3 #we check if nr can be divided by div
    for i in range(3,int(sqrt(nr)+1),2):
        if nr%div==0:return 0
    return 1

if __name__ == '__main__':
    n=int(input("Your number is: "))
    p1=n+1
    while is_prime(p1)*is_prime(p1+2)==0:
        p1+=1
    print(f"The closest twin prime numbers bigger than {n} are {p1} and {p1+2}.")