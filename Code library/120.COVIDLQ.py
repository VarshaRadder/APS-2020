# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:59:21 2020

@author: Varsha
"""
n=int(input())
for i in range(n):
    m=int(input())
    lst=list(map(int,input().split()))
    qq=[j for j in range(m) if lst[j]==1]
    c=0
    for j in range(len(qq)-1):
        if qq[j+1]-qq[j]<6:
            print("NO")
            break
        else:
            c+=1
    if c==len(qq)-1:
        print("YES")
