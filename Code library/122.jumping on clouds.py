# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:50:36 2020

@author: Varsha
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c,n):
    j=0
    b=0
    while(j<n-1):
        if(j+2>=n or c[j+2]==1):
            j=j+1
            b=b+1
        else:
            j=j+2
            b=b+1
    return b


n = int(input())
c = list(map(int, input().rstrip().split()))
print(jumpingOnClouds(c,n))
