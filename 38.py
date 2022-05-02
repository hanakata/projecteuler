# 配列を組み立て
def numberStick(list):
    numStr = ""
    for i in list:
        if i != '':
            numStr += str(i)
    return int(numStr)

# 配列内チェック
def arrayCheck(numList):
    for i in range(1, 10):
        if i not in numList:
            return False
    return True

# 数字配列を確認用配列に1つずつ追加
def arrayAppend(numList, splitNumberList):
    for i in splitNumberList:
        numList.append(i)
    return numList

# 数字を桁毎に配列化
def splitNumber(number):
    lst = []
    while number > 0:
        lst.append(number % 10)
        number //= 10
    lst.reverse()
    return lst

# 掛け算
def multiplication(i, j):
    return i * j

if __name__ == '__main__':
    ans = 0
    for i in range(1, 1000000):
        flg = True
        numList = []
        for j in range(1, 10):
            multiNum = multiplication(i, j)
            if len(str(multiNum)) == 1:
                numList.append(multiNum)
            else:
                numList = arrayAppend(numList, splitNumber(multiNum))
            if len(numList) > 9:
                flg = False
                break
            elif len(numList) == 9:
                break
        if not arrayCheck(numList):
            flg = False
        if flg:
           tmpAns = numberStick(numList)
           if ans < tmpAns:
               ans = tmpAns
print(ans)

