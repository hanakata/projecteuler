# 素数チェック(sieveは単純に遅い)
def primeNumberCheck(num):
    if num == 1:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# パンデジタル？チェック(Problem41用)
def pandigitalNumberCheck(num):
    numList = list(str(num))
    if str(0) in numList:
        return False
    for n in numList:
        if int(n) > len(numList):
            return False
    for i in range(1, 10):
        if numList.count(str(i)) >= 2:
            return False
    return True

if __name__ == '__main__':
    for i in reversed(range(1, 987654322)):
        if pandigitalNumberCheck(i):
            if primeNumberCheck(i):
                print(f'ans:{i}')
                break