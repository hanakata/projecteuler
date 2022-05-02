from sympy import sieve

# 素数チェック
def sieveCheck(num):
    return num in sieve

# 配列を組み立て
def numberStick(list):
    numStr = ""
    for i in list:
        if i != '':
            numStr += str(i)
    return int(numStr)

# 配列の1番目の値を削除
def listFrontDelete(list):
    if 1 < len(list):
        list.pop(0)
    return list

# 配列の最後の値を削除
def listLastDelete(list):
    if 1 < len(list):
        list.pop(-1)
    return list

# 数字を桁毎に配列化
def splitNumber(number):
    lst = []
    while number > 0:
        lst.append(number % 10)
        number //= 10
    lst.reverse()
    return lst

if __name__ == '__main__':
    ans = 0
    for i in range(10, 1000000):
        flg = True
        calList = []
        numList = splitNumber(i)
        calList.append(numberStick(numList))
        tmpList = numList
        for j in range(len(numList) - 1):
            tmpList = listFrontDelete(tmpList)
            calList.append(numberStick(tmpList))
        numList = splitNumber(i)
        tmpList = numList
        for j in range(len(numList) - 1):
            tmpList = listLastDelete(tmpList)
            calList.append(numberStick(tmpList))
        for check in calList:
            if sieveCheck(check):
                pass
            else:
                flg = False
                break
        if flg:
            print(i)
            ans += int(i)
    print(ans)

