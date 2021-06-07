# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 13:06:09 2021

@author: 片山雅利(softcreate)
"""

def arr_sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

def sum_excess_number(counter,sum_excess_numbers,excess_numbers):
    sum_excess_numbers_tmp = []
    if(len(sum_excess_numbers) == 0):
        sum_excess_numbers.append(counter * 2)
    else:
        for val in excess_numbers:
            sum_excess_numbers_tmp.append(val + counter)
        sum_excess_numbers = sum_excess_numbers + sum_excess_numbers_tmp
        del sum_excess_numbers_tmp
    sum_excess_set = set(sum_excess_numbers)
    sum_excess_numbers = list(sum_excess_set)
    return sum_excess_numbers

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

if __name__ == '__main__':
    sum_excess_numbers,excess_numbers = [],[]
    ans = 0
    for counter in range(2,28124):
        arr = make_divisors(counter)
        arr.pop(-1)
        value = arr_sum(arr)
        if counter < value:
            excess_numbers.append(counter)
            sum_excess_numbers = sum_excess_number(counter,sum_excess_numbers,excess_numbers)
        

    for counter in range(1,28124):
        if counter not in sum_excess_numbers:
            ans = ans + counter

    print(ans)

