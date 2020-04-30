# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:43:20 2020

@author: Varsha
"""

n=int(input())
lst=[[1,1],[2,2],[3,1],[1,3],[2,2],[3,3],[5,1],[1,5],[3,3],[4,4],[7,1],[1,7],[4,4],[5,5],[8,2],[2,8],[5,5],[6,6],[8,4],[4,8],[6,6],[7,7],[8,6],[6,8],[7,7],[8,8]]
lst1=[]
lst2=[]
for i in range(n):
    lst1=[]
    lst2=[]
    m,k=map(int,input().split())
    lst1.append([m,k])
    if m==k:
        lst2=lst1+lst
    else:
        mn=int((m+k)/2)
        lst1.append([mn,mn])
        lst2=lst1+lst
    print(len(lst2))
    for j in range(len(lst2)):
        print(lst2[j][0],"",lst2[j][1])
