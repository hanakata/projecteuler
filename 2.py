a, b, n = 1, 2, 0
while b < 4000000:
    if b % 2 == 0:
        n += b
    a, b = b, b + a
print(n)
