# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 13:06:09 2021

@author: 片山雅利(softcreate)
"""

import itertools

def createPermutation(numberArr):
    i = 1
    for v in itertools.permutations(numberArr):
        if i == 1000000:
            print(v)
            exit(0)
        i += 1

        

if __name__ == '__main__':
    question = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    createPermutation(question)