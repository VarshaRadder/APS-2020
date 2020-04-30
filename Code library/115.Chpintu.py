# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:39:44 2020

@author: Varsha
"""

n=int(input())
for o in range(n):
    e,f=map(int,input().split())
    qq=list(map(int,input().split()))
    yy={}
    pp=list(map(int,input().split()))
    for i in range(e):
        yy[qq[i]]=0
    for i in range(e):
        yy[qq[i]]+=pp[i]
    print(yy[min(yy, key=yy.get)])