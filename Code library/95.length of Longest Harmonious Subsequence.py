# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:49:29 2020

@author: Varsha
"""
import collections
def findLHS(nums):
        if not nums: return 0
        count = collections.Counter(nums)
        longest = 0
        for x in nums:
            if x-1 in count and count[x-1]+count[x] > longest:
                longest = count[x-1]+count[x]
        return longest
nums=list(map(int,input().split()))
print(findLHS(nums))