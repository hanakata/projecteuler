a, b, d, e, p, q = 1, 1, 1, 1, 1, 1
while p:
    c = a * a + b * b
    while q:
        if c < d * d:
            q = 0
        elif c == d * d:
            if a + b + d == 1000:
                print("a:" + str(a) + "b:" + str(b) + "c:" + str(d))
                print(a * b * d)
                p = 0
                break
        d += 1
    if b != 1000:
        b += 1
    else:
        a += 1
        b = a
    d = 1
    q = 1
