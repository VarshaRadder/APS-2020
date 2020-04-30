# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:35:06 2020

@author: Varsha
"""
def tribonacci(n):
        lst = [0, 1, 1]
        if n < 2:
            return lst[n]
        else:            
            for i in range(n-2):
                lst.append(sum(lst))
                lst.pop(0)
        return lst.pop()
n=int(input())
print(tribonacci(n))