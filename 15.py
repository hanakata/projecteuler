x, y = 20, 20
l = [[0 for i in range(x + 1)] for j in range(y + 1)]
l[0][0] = 1
for i in range(0, y + 1):
    for j in range(0, x + 1):
        if i == 0 or j == 0:
            l[i][j] = 1
        else:
            l[i][j] = l[i - 1][j] + l[i][j - 1]

print("Answer:" + str(l[x][y]))
