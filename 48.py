if __name__ == '__main__':
    ans_n = 0
    ans = ''
    for i in range(1, 1001):
        ans_n += i ** i
    for i in range(-10, 0):
        ans_s = str(ans_n)
        ans += ans_s[i]
    print(f'ans:{ans}')