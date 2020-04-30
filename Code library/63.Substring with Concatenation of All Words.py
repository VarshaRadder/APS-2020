# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:49:26 2020

@author: Varsha
"""
import collections

def findSubstring(S,W):
        if not W: return []
        LS, M, N, C = len(S), len(W), len(W[0]), collections.Counter(W)
        return [i for i in range(LS-M*N+1) if collections.Counter([S[a:a+N] for a in range(i,i+M*N,N)]) == C]
S=input()
W=list(input().split())
print(findSubstring(S,W))