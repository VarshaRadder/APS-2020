# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:05:19 2020

@author: Varsha
"""
def thirdMax(nums):
        
        unique_nums = set(nums)
		
		# return global max if unique number is not enough
        if len(unique_nums) < 3:
            return max( nums )

        # use native min-heap with negation to find maximal number
        unique_nums = [ -e for e in unique_nums]
        
        # build min-heap
        heapify( unique_nums )
        
        # pop 3rd maximum element
        for _ in range(3):
            value = heappop( unique_nums )
            
        return -value
nums=list(mao(int,input().split()))
print(thirdMax(nums))
