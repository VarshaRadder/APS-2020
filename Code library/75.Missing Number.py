# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:40:53 2020

@author: Varsha
"""

#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array

def missingNumber(nums):
        length = len(nums)    
        tot = length * (length+1) // 2    
        return (tot-sum(nums))
nums=list(mao(int,input().split()))
print(missingNumber(nums))