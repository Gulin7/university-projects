import math

n = int(input("n = "))
t0 = math.floor(math.sqrt(n))

print(f't0 = {t0}')

for i in range(1, 21):
    t = t0 + i
    value = t * t - n

    print(f't = t0 + {i}: t^2 - n = {value}')

    s = math.floor(math.sqrt(value))

    if s * s == value:
        print(f's={s} t={t}')
        break

print(f'n={t - s} * {t + s}')