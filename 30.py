# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:06:21 2022

@author: KatayamaMasa
"""
import sys

def check(num,num_arr):
    check_num = 0
    for i in num_arr:
        check_num += i ** 5
    if num == check_num:
        print(check_num)

if __name__ == "__main__":
    for num in range(1,1000000):
        x = [int(i) for i in str(num)]
        check(num, x)
