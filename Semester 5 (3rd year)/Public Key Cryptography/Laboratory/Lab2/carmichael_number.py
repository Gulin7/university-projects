import math

def isCarmichael(n):
    if n == 1:
        return '1'
    if n == 2:
        return 'prime'
    if n % 2 != 0:
        if all(n % k != 0 for k in range(3, math.ceil(n**0.5), 2)):
            return 'prime'
    elif all(pow(k, n, n) for k in range(1, n)):
        return 'carmichael'
    else:
        return 'non-carmichael composite'

def printAllCarmichaelLowerThanGivenBound(n):
    for number in range(1, n+1):
        if isCarmichael(number) == 'carmichael':
            print(number, " is a Carmichael number! 😎")

if __name__ == '__main__':
    while True:
        upperBound = input("Enter an integer upper bound: ")
        try:
            upperBound = int(upperBound)
            if upperBound < 1:
                print("Please enter a positive integer 🙅‍♂️")
            else:
                break
        except ValueError:
            print("You did not enter an integer 😾")
    print("Carmichael numbers lower than ", upperBound, " are:")
    printAllCarmichaelLowerThanGivenBound(upperBound)