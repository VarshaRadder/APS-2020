# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:00:20 2020

@author: Varsha
"""

def generate(numRows):
        ret = [[1]*(i+1) for i in range(numRows)]
        for r in range(2,numRows):
            for c in range(1,r):
                ret[r][c] = ret[r-1][c] + ret[r-1][c-1]
        return ret
numRows=int(input())
print(generate(numRows))