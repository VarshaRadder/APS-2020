# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:08:23 2020

@author: Varsha
"""
def maxProduct(nums):
        A, B = nums, nums[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(*A, *B)
nums=list(map(int,input().split()))
print(maxProduct(nums))