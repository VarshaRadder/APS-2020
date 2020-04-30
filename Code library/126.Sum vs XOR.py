# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:12:05 2020

@author: Varsha
"""



import math
import os
import random
import re
import sys

def sumXor(n):
    b=bin(n)[2:]
    t=0
    for i in range(len(b)-1,-1,-1):
        if b[i]=='0':
            t+=1
    if n>0:
        return 2**t
    else:
        return 1



n = int(input().strip())
result = sumXor(n)
print(result)