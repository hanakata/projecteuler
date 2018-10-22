x, y = 1, 1
l = []
for i in range(0, x + 1):
    for j in range(0, y + 1):
        if i == 0 and j == 0:
            l[i][j] = 0
        if i == 0 and j != 0:
            l[i][j] = 1
        if i != 0 and j == 0:
            l[i][j] = 1

print(l)
