# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:22:41 2020

@author: Varsha
"""

def subarraysDivByK(A,k):
    	D, s = {0:1}, 0
    	for a in A:
    		s = (s + a) % K
    		if s in D: D[s] += 1
    		else: D[s] = 1
    	return sum(i*(i-1)//2 for i in D.values())
A=list(map(int,input().split()))
k=int(input())
print(subarraysDivByK(A,k))
