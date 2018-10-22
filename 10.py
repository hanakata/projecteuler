import math
n = 2000000
a = []
for i in range(2, n + 1):
    a.append(i)
s = 0
p = a[s]
while p < math.sqrt(n):
    print(p)
    for j in a:
        print(j)
        if j == p:
            pass
        elif j % p == 0:
            a.remove(j)
    s += 1
    p = a[s]

print(a)
r = 0
for k in a:
    r += k

print(r)
