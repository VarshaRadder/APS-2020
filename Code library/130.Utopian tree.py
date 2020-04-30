# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:16:04 2020

@author: Varsha
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(x):
    height = 2**((n // 2) + 1) - 1
    return height if n % 2 == 0 else height*2



t = int(input())

for t_itr in range(t):
        n = int(input())
result = utopianTree(n)

print(result)