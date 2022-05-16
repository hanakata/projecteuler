# 素数チェック
def primeNumberCheck(num):
    if num == 1:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 数字を桁毎に配列化
def splitNumber(number):
    lst = []
    while number > 0:
        lst.append(number % 10)
        number //= 10
    lst.reverse()
    return lst

# 配列同士チェック
def arrayCheck(tmpList, checkList):
    for i in tmpList:
        if i not in checkList:
            return False
        else:
            checkList.remove(i)
    return True

# 項差マップ作成
def makeTermDiffMap(num1, num2, diffNum, tdmap):
    if diffNum not in tdmap:
        tdmap[diffNum] = str(num1) + str(num2)
    else:
        tdmap[diffNum] = tdmap[diffNum] + str(num1) + str(num2)
    return tdmap

# 項差計算
def calcTermDiff(num1, num2):
    dnum = 0
    if num1 < num2:
        dnum = num2 - num1
        return True, dnum
    return False, dnum

# 項差チェック
def checkTermDiff(numList):
    tdmap = {}
    for i in range(0, len(numList)):
        for j in range(0, len(numList)):
            if i >= j:
                continue
            else:
                check, num = calcTermDiff(numList[i], numList[j])
                if check:
                    tdmap = makeTermDiffMap(numList[i], numList[j], num, tdmap)
    return tdmap

if __name__ == '__main__':
    primeList = []
    for i in range(1000, 10000):
        if primeNumberCheck(i):
            primeList.append(i)
    p49List = []
    for i in range(0, len(primeList)):
        p49List.append(primeList[i])
        tmpList = splitNumber(primeList[i])
        for j in range(0, len(primeList)):
            if i == j:
                pass
            else:
                checkList = splitNumber(primeList[j])
                if arrayCheck(tmpList, checkList):
                    p49List.append(primeList[j])
        if len(p49List) > 3:
            ansList = []
            tmp = ''
            tdmap = checkTermDiff(p49List)
            for k, v in tdmap.items():
                if len(v) == 16:
                    tmp = v[0] + v[1] + v[2] + v[3]
                    ansList.append(tmp)
                    tmp = v[4] + v[5] + v[6] + v[7]
                    ansList.append(tmp)
                    tmp = v[8] + v[9] + v[10] + v[11]
                    ansList.append(tmp)
                    tmp = v[12] + v[13] + v[14] + v[15]
                    ansList.append(tmp)
                    if ansList[1] == ansList[2]:
                        print(ansList[0] + ansList[1] + ansList[3])
        p49List = []