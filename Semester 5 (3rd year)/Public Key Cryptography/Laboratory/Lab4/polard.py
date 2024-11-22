import math

x0 = int(input('x0 = '))
n = int(input('n = '))

f = lambda x: x * x + 1

x = [0] * 21

x[0] = x0

for i in range(1, 21):
    x[i] = f(x[i - 1]) % n
    print(f'x[{i}] = {x[i]}')

    if i % 2 == 0:
        abs_value = abs(x[i] - x[i // 2])
        gcd = math.gcd(abs_value, n)

        print(f'(x[{i}] - x[{i // 2}], n) is {gcd}')

        if gcd != 1:
            print(gcd, n // gcd)
            break