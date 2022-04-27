from sympy import sieve
import numpy as np

def sieveCheck(num):
    return num in sieve

def numberStick(list):
    numStr = ""
    for i in list:
        if i != '':
            numStr += str(i)
    return int(numStr)

def numConbination(numList):
    per_list = []
    for i in range(len(numList)):
        per_list.append(np.roll(numList, i))
    return per_list

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
        flg = True
        numList = splitNumber(i)
        per_list = numConbination(numList)
        for num in per_list:
            if sieveCheck(numberStick(num)):
                pass
            else:
                flg = False
                break
        if flg:
            ans += 1
    print(ans)
