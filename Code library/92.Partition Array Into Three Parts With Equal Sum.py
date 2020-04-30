# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:29:59 2020

@author: Varsha
"""
def canThreePartsEqualSum(A):        
        sumA,s,c = sum(A),0,0
        if sumA % 3 == 0:             
            while A and c<2:
                s += A.pop()
                if s*3 == sumA:
                    c += 1
                    s = 0
        return c == 2 and A and sum(A)*3==sumA
A=list(map(int,input().split()))
print(canThreePartsEqualSum(A))

