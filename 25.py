# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 13:06:09 2021

@author: 片山雅利(softcreate)
"""

def createFib():
    beforeFib = 1
    fib = 1
    for i in range(10000):
        nowFib = beforeFib + fib 
        if len(str(nowFib)) == 1000:
            print(i + 3)
            print(nowFib)
            exit(0)
        beforeFib = fib
        fib = nowFib
        
if __name__ == '__main__':
    createFib()