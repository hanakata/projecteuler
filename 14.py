p, i, b = 1, 2, 0
while p:
    r = []
    a = i
    while i != 1:
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3 * i + 1
        r.append(str(int(i)))
    if b < len(r):
        b = len(r)
        s = a
    i = a
    if i < 1000000:
        i += 1
    else:
        p = 0
print("Answer:" + str(s))
