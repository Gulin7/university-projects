def raise_to_power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return raise_to_power(x*x, n//2)
    else:
        return x * raise_to_power(x*x, n//2)


if __name__ == '__main__':
    print(raise_to_power(2, 12))
