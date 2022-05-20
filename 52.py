# 数字を桁毎に配列化
def splitNumber(number):
    lst = []
    while number > 0:
        lst.append(number % 10)
        number //= 10
    lst.reverse()
    return lst
# 配列比較
def arrComparison(numList1, numList2):
    for i in numList1:
        if i not in numList2:
            return False
        numList2.remove(i)
    if len(numList2) == 0:
        return True
    return False

if __name__ == '__main__':
    for i in range(100000, 100000000):
        flg = 0
        baseList = splitNumber(i)
        for j in range(2, 7):
            if flg == i:
                break
            numList2 = splitNumber(i * j)
            if len(baseList) != len(numList2):
                flg = 1
            else:
                if arrComparison(baseList, numList2):
                    pass
                else:
                    flg = 1
        if flg == 0:
            print(f'ans:{i}')
            import sys
            sys.exit()