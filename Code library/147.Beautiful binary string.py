# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:20:19 2020

@author: Varsha
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(a):
    ct, j = 0, 0
    while (j+3 <= len(a)):
        if a[j:j+3] == "010":
            ct, j = ct+1, j+3
        else: j += 1
    return ct



n = int(input())
b = input()
print(beautifulBinaryString(b))


