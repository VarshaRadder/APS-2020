# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:20:00 2020

@author: Varsha
"""
def intersection(nums1,nums2):
        return set(nums1).intersection(set(nums2))
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(intersection(nums1,nums2))


