N = 100000
# 素数チェック(sieveは単純に遅い)
def primeNumberCheck(num):
    if num == 1:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 平方数 * 2の引き算チェック
def checkSquareNumber(num):
    for i in range(1, N):
        snum = 2 * i * i
        if num < snum:
            return False
        check = num - snum
        if check == 0:
            return True
    return False

# 奇合成数チェック
def checkOddCompositeNumber(num):
    for i in range(1, N):
        if num < i:
            break
        if primeNumberCheck(i):
            pnum = num - i
            if checkSquareNumber(pnum):
                return False
    return True

if __name__ == '__main__':
    for i in range(1, N, 2):
        if primeNumberCheck(i):
            continue
        else:
            if checkOddCompositeNumber(i):
                print(f'ans:{i}')
                import sys
                sys.exit()
            else:
                print(f'not ans:{i}')