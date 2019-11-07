def main(num):
    ans = 1
    for i in range(1, num + 1):
        ans = ans * i
    result = calc(ans)
    print(result)


def calc(ans):
    a = 0
    for i in list(str(ans)):
        a += int(i)
    return a


if __name__ == "__main__":
    main(100)
