# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:24:47 2020

@author: Varsha
"""

def getNoZeroIntegers(n):
        return next([a, n - a] for a in range(n) if '0' not in str(a) + str(n - a))
n=int(input())
print(getNoZeroIntegers(n))