# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:55:26 2020

@author: Varsha
"""

from math import log
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False 
        res=round(log(n,2))
        return 2**res==n
        