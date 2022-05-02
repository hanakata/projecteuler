
# 配列を組み立て
def numberStick(list):
    numStr = ""
    for i in list:
        if i != '':
            numStr += str(i)
    return int(numStr)

# 配列を反対にする
def listreverse(numList):
    numList.reverse()
    return numList

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
    for i in range(1, 1000000):
        numList = splitNumber(i)
        perList = numberStick(numList)
        perReverseList = numberStick(listreverse(numList))
        if perList == perReverseList:
            # 2進数に変換して1桁ずつ配列に変換
            bnumList = list(format(perList, 'b'))
            bnumperList = numberStick(bnumList)
            bnumperReverseList = numberStick(listreverse(bnumList))
            if bnumperList == bnumperReverseList:
                print(i)
                ans += int(i)
    print(ans)