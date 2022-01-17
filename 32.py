# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:28:26 2022

@author: KatayamaMasa
"""

def check(i,j,ans):
    num = i * j
    if num in ans:
        return 0
    l = [0,0,0,0,0,0,0,0,0]
    x = [int(a) for a in str(num)]
    for s in str(i):
        x.append(int(s))        
    for s in str(j):
        x.append(int(s))        
    if 0 in x:
        return 0
    if len(x) > 9:
        return 0
    for n in x:
        if n == 1 and l[0] == 0:
            l[0] = 1
        elif n == 2 and l[1] == 0:
            l[1] = 1
        elif n == 3 and l[2] == 0:
            l[2] = 1
        elif n == 4 and l[3] == 0:
            l[3] = 1
        elif n == 5 and l[4] == 0:
            l[4] = 1
        elif n == 6 and l[5] == 0:
            l[5] = 1
        elif n == 7 and l[6] == 0:
            l[6] = 1
        elif n == 8 and l[7] == 0:
            l[7] = 1
        elif n == 9 and l[8] == 0:
            l[8] = 1
        else:
            return 0
    if 0 in l:
        return 0
    return num

if __name__ == "__main__":
    ans = []
    a = 0
    for i in range(2000):
        for j in range(2000):
            c = check(i,j,ans)
            if c != 0:
                ans.append(c)
    for l in ans:
        a = a + l
    print(a)
                
