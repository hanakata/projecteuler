stageCount = 15
j, k, l = 0, 0, 1
triArray = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
a = triArray[0][0]
ans = []
ans_t = []
ans_f = []
for i in range(1, stageCount):
    if len(ans) == 0:
        ans.append(str(a + triArray[i][0]) + ":" + str(0))
        ans.append(str(a + triArray[i][1]) + ":" + str(1))
    else:
        for s_t in ans:
            s = s_t.split(":")
            value = s[0]
            index = s[1]
            value_0 = str(
                int(value) + triArray[i][int(index)]) + ":" + str(index)
            value_1 = str(
                int(value) + triArray[i][int(index) + 1]) + ":" + str(int(index) + 1)
            ans_t.append(value_0)
            ans_t.append(value_1)
        ans = []
        for n in ans_t:
            ans.append(n)
        ans_t = []
for n in ans:
    s = n.split(":")
    ans_f.append(int(s[0]))
print(max(ans_f))
