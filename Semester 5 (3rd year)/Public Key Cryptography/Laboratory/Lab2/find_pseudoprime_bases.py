"""
Repeated Squaring Modular Exponentiation Algorithm:
a := 1;
if k = 0 then write(a);
c := b;
if k0 = 1 then a := b;
for i = 1 to t do
c := c2 mod n;
if ki := 1 then a := c ·a mod n;
write(a).
"""
def repeatedModularExponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def findBasesForWhichNumberIsPseudoprime(n):
    basesForWhichNumberIsPseudoprime = []
    for b in range(2, n):
        # If b is a pseudoprime base, add it to the list
        if repeatedModularExponentiation(b, n - 1, n) == 1:
            basesForWhichNumberIsPseudoprime.append(b)
    return basesForWhichNumberIsPseudoprime

# Example usage
if __name__ == '__main__':
    n = int(input("Enter an odd, composite number: "))
    basesForWhichNumberIsPseudoprime = findBasesForWhichNumberIsPseudoprime(n)
    print(f"The bases for which {n} is a pseudoprime are: {basesForWhichNumberIsPseudoprime}")
