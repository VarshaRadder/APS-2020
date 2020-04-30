# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:48:12 2020

@author: Varsha
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    count=0
    for i in range(len(a)):
        if a[i]<=0:
            count+=1
    if count>=k:
        return "NO"
    else:
        return "YES"

t = int(input())
for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)

