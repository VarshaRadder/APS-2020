# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:04:03 2020

@author: Varsha
"""

n=int(input())
for i in range(n):
    p=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    lst1.sort()
    lst2.sort()
    g=0
    for i in range(p):
        g+=min(lst1[i],lst2[i])
    print(g)