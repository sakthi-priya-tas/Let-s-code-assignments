# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:59:52 2020

@author: Sakthi priya TAS
"""

s=[int(s) for s in input().split()]
print(s)
for num in s:
    if num >= 0: 
       print(num, end = " ")