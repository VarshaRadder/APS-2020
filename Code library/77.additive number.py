# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:05:18 2020

@author: Varsha
"""
import itertools
#Additive number is a string whose digits can form additive sequence
def isAdditiveNumber(num):
    n = len(num)
    for i, j in itertools.combinations(range(1, n), 2):
        a, b = num[:i], num[i:j]
        if b != str(int(b)):
            continue
        while j < n:
            c = str(int(a) + int(b))
            if not num.startswith(c, j):
                break
            j += len(c)
            a, b = b, c
        if j == n:
            return True
    return False
num=input()
print(isAdditiveNumber(num))