# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:56:09 2020

@author: Varsha
"""
def findMedianSortedArrays(nums1, nums2):
        for j in range(len(nums2)):
            nums1.append(nums2[j])
        for i in range(len(nums1)):
            for j in range(i,len(nums1)):
                if nums1[i]>nums1[j]:
                    temp=nums1[i]
                    nums1[i]=nums1[j]
                    nums1[j]=temp
        if len(nums1)%2==0:
            n=len(nums1)//2
            med=float((nums1[n]+nums1[n-1])/2)
        else:
            n=len(nums1)//2
            med=nums1[n]
        return med
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(findMedianSortedArrays(nums1, nums2))