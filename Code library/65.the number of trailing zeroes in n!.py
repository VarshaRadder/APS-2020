# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:54:24 2020

@author: Varsha
"""

def trailingZeroes(n):
        i=5
        sum1=0
        while(n//i>=1):
            num=n//i
            sum1+=num
            i=i*5
        return sum1
n=int(input())
print(trailingZeroes(n))