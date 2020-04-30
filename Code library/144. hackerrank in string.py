# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:12:34 2020

@author: Varsha
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    s1="hackerrank"
    count=0
    j=0
    for i in range(len(s1)):
        flag=0
        while(flag==0 and j<len(s)):
            if s1[i]==s[j]:
                count+=1
                flag=1
            j+=1
    if count==len(s1):
        return "YES"
    else:
        return "NO"



q = int(input())

for q_itr in range(q):
        s = input()
result = hackerrankInString(s)
print(result)
