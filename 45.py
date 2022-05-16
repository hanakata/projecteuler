N = 100000
# 三角数の計算
def calcTriangularNumber(number):
    tnum = number * (number + 1) / 2
    return tnum

# 五角数の計算
def calcPentagonalNumber(number):
    pnum = number * (3 * number - 1) / 2
    return pnum

# 六角数の計算
def calcHexagonalNumber(number):
    hnum = number * (2 * number - 1)
    return hnum

if __name__ == '__main__':
    tNumberList = []
    pNumberList = []
    hNumberList = []
    for n in range(1, N):
        tNumberList.append(int(calcTriangularNumber(n)))
    for n in range(1, N):
        pNumberList.append(int(calcPentagonalNumber(n)))
    p_set = set(pNumberList)
    for n in range(1, N):
        hNumberList.append(int(calcHexagonalNumber(n)))
    h_set = set(hNumberList)

    for c in tNumberList:
        if c in p_set:
            if c in h_set:
                print(f'ans:{c}')