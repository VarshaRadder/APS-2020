# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:04:17 2020

@author: Varsha
"""
def splitArraySameAverage(A):
        A.sort()
        DP=[set() for _ in range(len(A)//2+1)]    
        for item in A:                 
            for count in range(len(DP)-2,-1,-1):          
                if len(DP[count])>0:                             
                    for a in DP[count]:
                        DP[count+1].add(a+item)
        for size in range(1,len(DP)):
            if all_sum*size/len(A) in DP[size]:
                return True
        return False
A=list(map(int,input().split()))
print(splitArraySameAverage(A))
