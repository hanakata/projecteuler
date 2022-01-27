# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:09:18 2022

@author: KatayamaMasa
"""

def hoge():
    numer, denom = 1, 1
    _duplicate = lambda a, b: set(list(str(a))) & set(list(str(b)))
    _replace = lambda a, b: float(str(a).replace(str(b), '', 1))
    for a in range(11, 100):
        if a % 10 == 0: continue
        for b in range(a+1, 100):
            if b % 10 == 0: continue
            duplicate_num = _duplicate(a, b)
            for n in duplicate_num:
                if float(a) / b == _replace(a, n) / _replace(b, n):
                    numer, denom = numer * a, denom * b
    return denom // gcd(numer, denom)

def gcd(a, b): # 最大公約数取得
    while b:
        a, b = b, a%b
    return a

print(hoge())