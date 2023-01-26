from math import sqrt
def is_prime(p):
    """
    This functions check whether a number is prime or not.

    :param p: the number whose primality we check
    :return: returns 1 if the nr is prime and 0 if its not
    """
    if p==2:return 1
    if p<2 or p%2==0:return 0
    stop=int(sqrt(p))+1
    for div in range(3,stop,2):
        if p%div==0:return 0
    return 1

if __name__ == '__main__':
    n=int(input("Enter your number: "))
    if is_prime(n-2) != 0:
        print(f"Our number can be written as {2} + {n-2}.")
    else:
        for i in range(3,n,2):
            if is_prime(i)*is_prime(n-i)!=0:
                print(f"Our number can be written as {i} + {n-i}.")
                break
