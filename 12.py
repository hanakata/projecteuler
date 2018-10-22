i, a, b, f = 1, 0, 1, 0

while f < 500:
    l = []
    a += i
    while a >= b:
        if b in l:
            break
        if a % b == 0:
            l.append(b)
            c = a / b
            if int(c) not in l:
                l.append(int(c))
        b += 1
    f = len(l)
    i += 1
    b = 1
print("Answer:" + str(a))
