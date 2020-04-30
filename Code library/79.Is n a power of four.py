# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:12:00 2020

@author: Varsha
"""

from math import log
def isPowerOfFour(num):
        if(num<=0):return False
        res=round(log(num,4))
        return 4**res==num
num=int(input())
print(isPowerOfFour(num))
