# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:58:00 2020

@author: Varsha
"""

def numSubarrayProductLessThanK(nums,k):
        res = 0
        subArrProd = 1 
        left = 0

        for right, rightNum in enumerate(nums):
            subArrProd *= rightNum         
            while subArrProd >= k and left <= right:
                subArrProd //= nums[left]
                left += 1

            if subArrProd < k:
                l = right+1-left 
                res += l
            else: 
                pass
        return res
nums=list(map(int,input().split()))
k=int(input())
print(numSubarrayProductLessThanK(nums,k))