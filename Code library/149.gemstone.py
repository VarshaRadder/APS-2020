# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:28:01 2020

@author: Varsha
"""

n = int(input())
s1 = set(input())

for i in range(n-1):
    s2 = set(input())
    s1 = s1 & s2

print(len(s1))
