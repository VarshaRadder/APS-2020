# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:23:02 2020

@author: Varsha
"""

def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input())
num2 = int(input())

print("The H.C.F. is", compute_hcf(num1, num2))