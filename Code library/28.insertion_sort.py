# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:01:00 2020

@author: Varsha
"""

import random
n=int(input("enter the number of elements"))
a = [random.randint(0,100) for i in range(n)]
print(a)

for i in range(1,n):
 r=a[i]
 j=i-1
 while(j>=0 and a[j]>r):
     a[j+1]=a[j]
     j=j-1
     a[j+1]=r

print(a)
