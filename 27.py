# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:30:06 2022

@author: KatayamaMasa
"""

import math

def is_prime(n):
    if n == 1 or n == 0: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def calc(a,b,n):
    ans = n ** 2 + a * n + b
    if is_prime(ans) == False:        
        print(a * b)
        return False
    return True

if __name__ == "__main__":
    i = 0
    for a in range(1000):
        for b in range(1001):
            for n in range(500):
                i = i + 1
                if calc(a,b,n) == False:
                    print(i)
                    i = 0
                    break
                    

    