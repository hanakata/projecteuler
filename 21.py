def main(num):
    for i in range(1, num):
        divisorSum1 = divisorCalc(i)
        if divisorSum1 != 0:
            divisorSum2 = divisorCalc(divisorSum1)
            if i == divisorSum2:
                if divisorSum1 != divisorSum2:
                    print(divisorSum1)
                    print(divisorSum2)


def divisorCalc(num):
    divisorArray = []
    divisorSum = 0
    for i in range(1, num):
        if num % i == 0:
            divisorArray.append(i)
    if len(divisorArray) > 0:
        divisorSum = sum(divisorArray)
    return divisorSum


if __name__ == "__main__":
    main(10000)
