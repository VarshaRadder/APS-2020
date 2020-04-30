# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:08:59 2020

@author: Varsha
"""
from math import log
def isPowerOfThree(n):        
        if n<=0:return False
        res=round(log(n,3))
        return 3**res==n
    
n=int(input())
print(isPowerOfThree(n))
