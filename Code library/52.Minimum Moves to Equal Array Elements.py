# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:41:37 2020

@author: Varsha
"""

nums=list(map(int,input().split()))
minimum = min(nums)
length= len(nums)
total=sum(nums)
print(total- length*minimum)