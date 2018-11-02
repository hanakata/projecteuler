digest = 1000
i, r, a = 1, 2, 0
while i < digest:
    r = r * 2
    i += 1

for i in list(str(r)):
    a += int(i)
print("Answer:" + str(a))
