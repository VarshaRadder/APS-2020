# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:06:21 2020

@author: Varsha
"""

n=int(input())
for i in range(n):
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    lst4=[0]*lst1[0]
    flag=0
    count=1
    for j in range(lst1[0]):
        if max(lst2)>lst1[1]:
            lst4[lst2.index(max(lst2))]=1
            flag=1
            break
        if lst1[1]%lst2[j]!=0:
            lst4[j]=lst1[1]//lst2[j]+1
            flag=1
            break
    if lst1[0]==1:
        count=0
        if lst1[1]%lst2[0]==0:
            flag=0
    if flag!=1 and count!=0:
        for j in range(lst1[0]-1):
            if lst2[j+1]%lst2[j]!=0:
                lst4[j+1]=lst1[1]//lst2[j+1]-1
                lst1[1]-=((lst1[1]//lst2[j+1])-1)*lst2[j+1]
                lst4[j]=lst1[1]//lst2[j]+1
                break

    if sum(lst4)==0 and flag==0:
        print("NO")
    else:
        lst4.insert(0,"YES")
        for j in range(len(lst4)):
            #print(type(lst4[j]))
            print(lst4[j],end=' ')
        print(' ')