N = 10000
# 五角数同士の足し算
def additionPentagonalNumber(n1, n2, list, setList):
    checkNum = list[n1] + list[n2]
    if checkNum in setList:
        print(f'add check:{checkNum}')
        return True
    return False

# 五角数同士の引き算チェック
def subtractionPentagonalNumber(n1, n2, list, setList):
    checkNum = list[n2] - list[n1]
    if checkNum < 0:
        return False
    if checkNum in setList:
        return True
    return False

# 五角数の計算
def calcPentagonalNumber(number):
    pnum = number * (3 * number - 1) / 2
    return pnum

if __name__ == '__main__':
    pNumberList = []
    for n in range(1, N):
        pNumberList.append(int(calcPentagonalNumber(n)))
    print('done')
    p_set = set(pNumberList)
    for i in range(0, N - 1):
        for j in range(0, N - 1):
            if i >= j:
                continue
            else:
                if subtractionPentagonalNumber(i, j, pNumberList, p_set):
                    if additionPentagonalNumber(i, j, pNumberList, p_set):
                        print(f'ans:{pNumberList[j] - pNumberList[i]}')
                        import sys
                        sys.exit()

