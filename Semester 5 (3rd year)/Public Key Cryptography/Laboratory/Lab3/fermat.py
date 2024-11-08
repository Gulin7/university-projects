import math

def isSquare(n):
    return math.isqrt(n) ** 2 == n

def fermat_factorization(n):
    print(f"Starting factorization for n = {n}")

    if n % 2 == 0:
        print("n is even, returning (2, n // 2)")
        return (2, n // 2)

    k = 1
    while True:
        product = n * k
        print(f"Trying k = {k}, product = {product}")

        t = math.isqrt(product) + 1
        for i in range(5):
            # Check if t^2 - product is a perfect square
            b_squared = t * t - product
            if isSquare(b_squared):
                b = math.isqrt(b_squared)
                print(f"n = ({t} + {b}) * ({t} - {b})")

                factor1 = math.gcd(n, t + b)
                factor2 = n // factor1
                print(f"Factors found: {factor1} and {factor2}")
                return (factor1, factor2)
            t += 1

        k += 1
        print(f"No factors found for k = {k - 1}, increasing k.\n")


# Example usage
n = 243947
factors = fermat_factorization(n)
print(f"Factors of {n} are: {factors}")
