# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:07:24 2020

@author: Varsha
"""
'''
A k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k
'''

def find_pairs(L,k):

    L.sort()

    N = len(L)

    i = pairs = 0
    j = 1

    while j < N:
        if j < N - 1 and L[j] == L[j + 1]:
            j += 1

        elif L[j] == L[i] + k:
            pairs += 1
            i += 1
            j += 1

        elif L[j] > L[i] + k:
            i += 1

        elif L[j] < L[i] + k:
            j += 1

        j = max(j, i + 1)

    return pairs
L=list(map(int,input().split()))
k=int(input())
print(find_pairs(L,k))