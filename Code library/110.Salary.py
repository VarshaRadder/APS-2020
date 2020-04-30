# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:47:14 2020

@author: Varsha
"""
n = int(input())
for j in range(n):
    m = int(input())
    lst = list(map(int, input().split()))
    mn=min(lst)
    le=len(lst)
    to=sum(lst)
    print(to-le*mn)

