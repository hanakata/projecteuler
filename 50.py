# 素数チェック
def primeNumberCheck(num):
    if num == 1:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    primeList = []
    for i in range(2,1000000):
        if primeNumberCheck(i):
            primeList.append(i)
    start = 0
    topTerm = 0
    while True:
        ans_s = 0
        term_t = 0
        if start == len(primeList):
            print(topTerm)
            import sys
            sys.exit()
        for i in range(start, len(primeList)):
            ans_s += primeList[i]
            term_t += 1
            if ans_s > 1000000:
                break
            if primeNumberCheck(ans_s):
                term = term_t
                ans = ans_s
        if topTerm < term:
            topTerm = term
        print(f'ans:{term} {ans}')
        start += 1
