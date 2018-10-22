a = 0

for i in range(1, 1000):
    division3 = i % 3
    division5 = i % 5
    if division3 == 0:
        a += i
    elif division5 == 0:
        a += i

print(a)
