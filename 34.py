import math
def numFactorial(numList):
    sumNum = 0
    for i in numList:
        sumNum += math.factorial(int(i))
    return sumNum

def splitNumber(number):
    lst = []
    while number > 0:
        lst.append(number % 10)
        number //= 10
    lst.reverse()
    return lst

if __name__ == '__main__':
    ans = 0
    for i in range(2, 10000000):
        numList = splitNumber(i + 1)
        sumNum = numFactorial(numList)
        if i + 1 == sumNum:
            ans += sumNum
            print("loop:" + str(ans))
    print(ans)

