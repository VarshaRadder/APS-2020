# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:38:42 2020

@author: Varsha
"""
def isUgly(num):
        if num==0:
            return False
        for i in [2,3,5]:
            while num%i==0:
                num/=i
        return num==1
num=int(input())
print(isUgly(num))