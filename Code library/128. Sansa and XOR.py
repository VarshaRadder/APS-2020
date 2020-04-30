# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:20:21 2020

@author: Varsha
"""

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
def sansaXor(arr):
    if len(arr)%2==0:
        return 0
    else:
        y=0
        for j in range(0,len(arr),2):
            y=y^arr[j]
        return y


t = int(input())

for t_itr in range(t):
        n = int(input())
arr = list(map(int, input().rstrip().split()))
result = sansaXor(arr)
print(result)