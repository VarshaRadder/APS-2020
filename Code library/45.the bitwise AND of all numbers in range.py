# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:40:50 2020

@author: Varsha
"""
import math
m=int(input())
n=int(input())
print((m & n & - (2 << math.floor(math.log2(n-m))) if m != n else m))