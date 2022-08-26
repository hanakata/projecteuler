# 階乗の計算
def calcFactorial(num):
    fnum = 0
    for i in reversed(range(1, num + 1)):
        if fnum == 0:
            fnum = i
        else:
            fnum = fnum * i
    return fnum

# 組み合わせ数の計算
def numberOfCombinations(n, r):
    nFactorial = calcFactorial(n)
    rFactorial1 = calcFactorial(r)
    rFactorial2 = calcFactorial(n - r)
    rFactorial = rFactorial1 * rFactorial2
    return nFactorial / rFactorial

if __name__ == '__main__':
    ans = 0
    for n in range(1, 101):
        for r in range(1, 101):
            if n > r:
                calcNum = numberOfCombinations(n, r)
                if 1000000 < calcNum:
                    ans += 1
    print(f'ans:{ans}')