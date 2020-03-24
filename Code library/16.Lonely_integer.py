# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:16:15 2020

@author: Varsha
"""



import math
import os
import random
import re
import sys


def lonelyinteger(a):
    if len(a)==1:
        return a[0]
    i=0
    while(i<len(a)):
        if a[i]!=1:
            b=[]
            b=a[i+1:]+a[:i]
            if a[i] not in b:
                return a[i]
        i=i+1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
