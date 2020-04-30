# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:41:48 2020

@author: Varsha
"""

def subarraySum(nums,k):

        count = 0
        total = 0
        sums_map = {}
        sums_map[0] = 1
        
        for num in nums:
            total += num
            if sums_map.get(total-k):
                count = count + sums_map.get(total-k)

            sums_map[total] = 1 + sums_map.get(total, 0) 

        return count
nums=list(map(int,input().split()))
k=int(input())
