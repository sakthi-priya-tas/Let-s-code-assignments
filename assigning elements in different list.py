# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:17:44 2020

@author: Sakthi priya TAS
"""

#assigning elements to different lists
list1 = [2,3,4,5]
list1.insert(5,3)
list2 = [11,12,13,15]
list2.insert(1,45)

#accessing elements from tuple
tup1 = (1,'a',2,'b',3,'c')
print(tup1[0:5])

#deleting different dictionary elements
myDict = {"a1":"1","a2":"2","a3":3}
print(myDict.get("a3"))
del myDict["a2"]
print(myDict)