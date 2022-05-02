SUM_EDGE = 1000

# 直角三角形となるか確認
def validationRightTriangle(a, b, c):
    aSquare = a * a
    bSquare = b * b
    cSquare = c * c
    if aSquare + bSquare == cSquare:
        return True
    else:
        return False

# 3辺目の長さを計算
def calcEdge(a, b):
    c = SUM_EDGE - (a + b)
    return c

if __name__ == '__main__':
    t_ans = 0
    for SUM_EDGE in range(1, 1001):
        i = 0
        print(SUM_EDGE)
        for a in range(1, 1000):
            for b in range(1, 1000):
                if a + b < SUM_EDGE:
                    c = calcEdge(a, b)
                    if validationRightTriangle(a, b, c):
                        i += 1
        if t_ans < i:
            t_ans = i
            ans = SUM_EDGE
    print("ans:" + str(ans))






