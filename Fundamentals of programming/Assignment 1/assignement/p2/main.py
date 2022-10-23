def palindrome(n):
    """
    This functions returns the palindrome of a given number.

    It takes the digits from right to left and add to the palindrome in this order.
    :param n: the number whose palindrome we are computing
    :return: the palindrome of n
    """
    pal=0
    while n>0:
        pal=pal*10+n%10
        n=n//10
    return pal

if __name__=='__main__':
    n=int(input("Your chosen number is: "))
    palin=palindrome(n)
    print(f"The palindrome of {n} is {palin}.")