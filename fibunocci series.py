# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:59:52 2020

@author: Sakthi priya TAS
"""

a=int(input("Enter the number terms"))
f=0
s=1
if a<=0:
    print("The series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        n=f+s                           
        print(n,end=" ")
        f=s
        s=n