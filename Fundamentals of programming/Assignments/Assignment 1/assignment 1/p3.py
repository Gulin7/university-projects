# Solve the problem from the third set here
from math import sqrt
def is_prime(n):
    """
    This functions checks if a number is prime or not.

    It returns 1 for num 2, then 0 for the left even numbers and those lower than 2. Then it checks if the num
    has any odd divisors, in which case it would return 0 ( cause the number is not prime ).
    :param n: the number whose primality we check
    :return: 1 if a number is prime, 0 if its not
    """
    if n==2: return 1
    if n<2 or n%2==0: return 0
    stop = int(sqrt(n)) + 1
    for div in range(3, stop, 2):
        if n % div == 0: return 0

def factors(n,num):
    """
    Returns how many steps are left and the number we are currently on.

    :param n: how many steps we have left to go over to get to the element of the sequence we need to print
    :param num: the number whose prime divisors we are checking
    :return: return n and prints the element if n==0
    """
    div=2
    while div<=num:
        if num%div==0:
            while num%div==0:
                num=num//div
            n=n-div
            if n<=0: return n,div
        div=div+1
    return n,div

if __name__=='__main__':
    n=int(input("Pick a number: "))
    n-=1 #we won't check 1
    if n==0: print(f"The element is 1.")
    else:
        aux=0
        current=2 # The current element whose prime divisors we are searching for
        while n>0:
            if is_prime(current)!=0:
                n=n-1
                if n==0: print(current)
            else:
                n,aux=factors(n,current)
                if n<=0: print(aux)
            current+=1