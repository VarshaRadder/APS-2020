# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:04:02 2020

@author: Varsha
"""
n=int(input())
for k in range(n):
    m=int(input())
    arr=list(map(int,input().split()))
    s=0
    flag=0
    count=0
    lst=[]
    lst1=[]
    for i in range(len(arr)):
        if arr[i]%2!=0:
            count+=1
        else:
            flag=1
        if flag==1 or i==len(arr)-1:
            flag=0
            s+=((count*(count+1))// 2)
            count=0
    for i in range(len(arr)):
        if arr[i]%4==0:
            if len(lst)==0:
                s+=i*(len(arr)-i)+1+len(arr)-1-i
                lst.append(i)
                if len(lst1)==1:
                    lst1.pop(0)
            elif len(lst)==1:
                s+=(i-lst[0]-1)*(len(arr)-i)+1+len(arr)-1-i
                lst.pop(0)
                lst.append(i)
                if len(lst1)==1:
                    lst1.pop(0)
        if arr[i]%2==0 and arr[i]%4!=0:
            lst1.append(i)
            if len(lst1)==2 and len(lst)==0:
                s+=(lst1[0])*(len(arr)-lst1[1])+1+(len(arr)-lst1[1]-1)
                lst.append(lst1[0])
                lst1.pop(0)
            elif len(lst1)==2 and len(lst)>0:
                s+=(lst1[0]-lst[0]-1)*(len(arr)-lst1[1])+1+(len(arr)-lst1[1]-1)
                lst.pop(0)
                lst.append(lst1[0])
                lst1.pop(0)
    print(s)
