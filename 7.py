p, n, v = 1, 2, 0
a = []
while p:
    for i in range(2, n + 1):
        if n != i:
            s = n % i
        else:
            s = 1
        if s == 0:
            v = 1
            break
    if v == 0:
        a.append(n)
        if len(a) == 10001:
            print(a[-1])
            p = 0
    n = n + 1
    v = 0
