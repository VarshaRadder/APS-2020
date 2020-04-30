# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:35:10 2020

@author: Varsha
"""
def twoSum(nums,target):
        list1=[]
        for i,j in enumerate(nums):
            for k in range(i+1,len(nums)):
                if j+nums[k]==target:
                    list1.append(i)
                    list1.append(k)
        return list1
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target))