# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:29:02 2020

@author: Varsha
"""

import math
import os
import random
import re
import sys


def diagonalDifference(arr,n):
    # Write your code here
    sum2=0
    sum1=0
    for i in range(n):
        for j in range(n):
            if i==j:
                sum2+=arr[i][i]
            if i+j==(n-1):
                sum1+=arr[i][j]
    sub=abs(sum2-sum1)
    return sub



n = int(input().strip())
arr = []
for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
print(diagonalDifference(arr,n))
