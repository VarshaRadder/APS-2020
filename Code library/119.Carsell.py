# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:58:34 2020

@author: Varsha
"""

n=int(input())
for i in range(n):
    m=int(input())
    lst=list(map(int,input().split()))
    lst.sort(reverse=True)
    sum=lst[0]
    for j in range(1,m):
        lst[j]-=j
        if lst[j]>0:
            sum+=lst[j]
    print(sum%(1000000007))