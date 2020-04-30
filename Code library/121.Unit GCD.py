# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:02:46 2020

@author: Varsha
"""
n=int(input())
for i in range(n):
    m=int(input())
    if m==1:
        print(1)
        lst=[1,1]
        print(' '.join(map(str, lst)))
    else:
        print(m//2)
        if(m%2)!=0:
            lst=[3,1,2,3]
            print(' '.join(map(str, lst)))
            for j in range(4,m,2):
                lst=[2,j,j+1]
                print(' '.join(map(str, lst)))
        else:
            lst=[2,1,2]
            print(' '.join(map(str, lst)))
            for j in range(3,m,2):
                lst=[2,j,j+1]
                print(' '.join(map(str, lst)))
