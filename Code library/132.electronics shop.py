# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:56:14 2020

@author: Varsha
"""

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(ke, dr, b):
    #
    # Write your code here.
    #
    dif=10000
    sum=0
    a=-1
    for i in range(len(ke)):
        for j in range(len(dr)):
            if(ke[i]+dr[j]<=b):
                sum=ke[i]+dr[j]
                #print(sum)
                if b-sum<dif:
                    a=sum
                    dif=b-sum
    return a  
            

bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
print(getMoneySpent(keyboards, drives, b))
