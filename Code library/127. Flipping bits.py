# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:19:31 2020

@author: Varsha
"""
import math
import os
import random
import re
import sys
import math
# Complete the flippingBits function below.
def flippingBits(num):
    return ~ num + (1 << 32)

q = int(input())

for q_itr in range(q):
        n = int(input())
result = flippingBits(n)
print(result)
