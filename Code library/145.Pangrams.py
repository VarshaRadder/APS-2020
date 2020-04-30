# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:14:35 2020

@author: Varsha
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(st):
    st=st.lower()
    s=list(st.split())
    l=[]
    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j].upper()
            if s[i][j] not in l and s[i][j]!=' ':
                l.append(s[i][j])
    if len(l)==26:
        return "pangram"
    else:
        return "not pangram" 

st=input()
print(pangrams(st))