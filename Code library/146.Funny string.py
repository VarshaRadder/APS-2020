# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:16:57 2020

@author: Varsha
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    lst1=[]
    lst2=[]
    di1=[]
    di2=[]
    for i in range(len(s)):
        lst1.append(ord(s[i]))
    s1=s[::-1]
    for i in range(len(s1)):
        lst2.append(ord(s1[i]))
    for i in range(len(lst1)-1):
        di1.append(abs(lst1[i]-lst1[i+1]))
    for i in range(len(lst2)-1):
        di2.append(abs(lst2[i]-lst2[i+1]))   

    if di1==di2:
        return "Funny"
    else:
        return "Not Funny"




q = int(input())
for q_itr in range(q):
        s = input()

        result = funnyString(s)
        print(result)
