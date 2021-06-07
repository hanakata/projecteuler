# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:18:35 2021

@author: 片山雅利(softcreate)
"""

l = list('0ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ans = 0
with open("name.txt") as f:
    s = f.read()
    s_arr = s.split(',')
    i = 0
    for name in sorted(s_arr):
        i += 1
        name_list = list(name.replace('"',""))
        num = 0
        for m in name_list:
            num += l.index(m)
        a = num * i
        ans += a

print(ans)

    