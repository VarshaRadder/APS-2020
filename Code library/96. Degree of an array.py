# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:44:30 2020

@author: Varsha
"""
def findShortestSubArray(nums):
        d = dict()
        for i, num in enumerate(nums):
            freq, first_occur, last_occur = d.get(num, (0, i, i))
            d[num] = (freq + 1, first_occur, i)
        
        freq, first_occur, last_occur = max(d.values(), key=lambda x: (x[0], x[1]-x[2]))
        return last_occur - first_occur + 1
nums=list(map(int,input().split()))
print(findShortestSubArray(nums))