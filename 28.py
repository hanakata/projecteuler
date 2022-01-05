# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:09:19 2022

@author: KatayamaMasa
"""

if __name__ == "__main__":
    ans = 0
    for i in range(3,1002,2):
        n1 = i * i
        n2 = n1 - (i - 1)
        n3 = n2 - (i - 1)
        n4 = n3 - (i - 1)
        ans = n1 + n2 + n3 + n4 + ans
    print(ans + 1)