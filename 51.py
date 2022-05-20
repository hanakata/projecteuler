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

# 配列を組み立て
def numberStick(list):
    numStr = ""
    for i in list:
        if i != '':
            numStr += str(i)
    return int(numStr)

if __name__ == '__main__':
    for i in range(1000, 10000000):
        flg = 0
        ansArr = []
        count = 0
        numList = splitNumber(i)
        if numList.count(0) > 1:
            flg = 1
            base = 0
        if numList.count(1) > 1:
            flg = 1
            base = 1
        if numList.count(2) > 1:
            flg = 1
            base = 2
        if flg == 1:
            num = str(numberStick(numList))
            for j in range(base, 10):
                checkNum = num.replace(str(base), str(j))
                if primeNumberCheck(int(checkNum)):
                    count += 1
                    ansArr.append(checkNum)
        if count == 8:
            print(f'ans: {count} {ansArr}')
            break