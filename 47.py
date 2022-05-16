N = 1000000
# 素因数分解
def primeFactorize(n):
    primeList = []
    if n == 1:
        primeList.append(1)
    while n % 2 == 0:
        primeList.append(2)
        # //で整数化
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            primeList.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        primeList.append(n)
    return primeList

if __name__ == '__main__':
    check = 0
    ansList = []
    for i in range(1, N):
        primeList = primeFactorize(i)
        if len(set(primeList)) == 4:
            check += 1
            ansList.append(i)
        else:
            check = 0
            ansList = []
        if check == 4:
            print(f'ans:{ansList[0]}')
            import sys
            sys.exit()
