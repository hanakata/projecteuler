

# 配列の指定位置を組み立て
def numberStick(n1, n2, n3):
    numStr = ""
    numStr += str(n1)
    numStr += str(n2)
    numStr += str(n3)
    return int(numStr)

# problem43の性質チェック
def p043Nature(num):
    numList = list(str(num))
    if numberStick(numList[1], numList[2], numList[3]) % 2 != 0:
        return False
    if numberStick(numList[2], numList[3], numList[4]) % 3 != 0:
        return False
    if numberStick(numList[3], numList[4], numList[5]) % 5 != 0:
        return False
    if numberStick(numList[4], numList[5], numList[6]) % 7 != 0:
        return False
    if numberStick(numList[5], numList[6], numList[7]) % 11 != 0:
        return False
    if numberStick(numList[6], numList[7], numList[8]) % 13 != 0:
        return False
    if numberStick(numList[7], numList[8], numList[9]) % 17 != 0:
        return False
    return True

# パンデジタルチェック
def pandigitalNumberCheck(num):
    numList = list(str(num))
    for i in range(0, 10):
        if numList.count(str(i)) >= 2:
            return False
    return True

if __name__ == '__main__':
    ans = 0
    for i in range(1234567890, 9999999999):
        if p043Nature(i):
            if pandigitalNumberCheck(i):
                print(i)
                ans += i
    print(f'ans{ans}')
