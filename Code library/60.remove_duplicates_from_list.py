# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:16:46 2020

@author: Varsha
"""

def removeDuplicates(nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
nums=list(map(int,input().split()))
print(removeDuplicates(nums))