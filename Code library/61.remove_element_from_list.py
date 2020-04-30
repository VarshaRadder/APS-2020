# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:20:31 2020

@author: Varsha
"""
def removeElement(nums,val):
        i=0
        while(i<len(nums)):
            if nums[i]==val:
                del nums[i]
            else:
                i+=1
        return len(nums)
nums=list(map(int,input().split()))
val=int(input())
print(removeElement(nums,val))