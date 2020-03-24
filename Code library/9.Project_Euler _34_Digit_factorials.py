# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:24:08 2020

@author: Varsha
"""
fact=[1,1,2,6,24,120,720,5040,40320,362880]
n=int(input())
lst4=[]
for i in range(19,n):
    j=i
    lst=[]
    while(j>0):
        lst.append(j%10)
        j=j//10
    lst3=[]
    for k in range(len(lst)):
        lst3.append(fact[lst[k]])
    if(sum(lst3)%i==0):
        lst4.append(i)
if len(lst4)==0:
    print(0)
else:
    print(sum(lst4))

