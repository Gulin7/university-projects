#Problem 1 from set 1
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
    while div*div <=nr :
        if nr%div==0: return 0
        div+=2
    return 1

if __name__=='__main__':
    n=int(input("Your chosen number: "))
    prime=n+1 #we use this variable to generate the first prime number larger than n
    while is_prime(prime)==0:
     prime+=1
    print(f"The first prime number larger than {n} is {prime}")