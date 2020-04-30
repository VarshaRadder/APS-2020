# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:47:14 2020

@author: Varsha
"""
n=int(input())
for i in range(n):
    m=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    a=max(lst1)
    b=max(lst2)
    if a>b or b>a:
        print("YES")
    else:
        print("NO")
