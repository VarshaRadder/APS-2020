# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:15:29 2020

@author: Varsha
"""
def dominantIndex(nums):
        
        max_now = second = -1
        
        index = 0
        
        for i in range(0,len(nums)):
            if nums[i] > max_now:
                second = max_now
                index = i
                max_now = nums[i]
            elif nums[i] != max_now:                    
                if nums[i] > second:
                    second = nums[i]
        
        if max_now >= second*2:
            return index
        return -1
nums=list(map(int,input().split()))
if dominantIndex(nums)==-1:
    print("No number")
else:
    print(nums[dominantIndex(nums)])