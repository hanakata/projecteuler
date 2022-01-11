# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:58:45 2022

@author: KatayamaMasa
"""

if __name__ == "__main__":
    l = []
    for i in range(2,101):
        for j in range(2,101):
            l.append(i**j)
    print(len(set(l)))