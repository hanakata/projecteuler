n = 2520
p = 1
while p:
    for i in range(1, 21):
        s = n % i
        if s == 0:
            if i == 20:
                p = 0
        else:
            n += 1
            break
print(n)
