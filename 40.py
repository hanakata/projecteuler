# 数字配列を確認用配列に1つずつ追加
def arrayAppend(numList, splitNumberList):
    for i in splitNumberList:
        numList.append(i)
    return numList

if __name__ == '__main__':
    numList = [0]
    for i in range(1, 100000000):
        tList = list(str(i))
        decimalList = arrayAppend(numList, tList)
        if len(decimalList) > 1000001:
            break
    calcNoList = [1, 10, 100, 1000, 10000, 100000, 1000000]
    ans = 1
    for i in calcNoList:
        ans = ans * int(decimalList[i])
    print(f'ans:{ans}')
