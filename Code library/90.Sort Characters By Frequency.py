# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:26:41 2020

@author: Varsha
"""

import collections
def frequencySort(s):
        """
        :type s: str
        :rtype: str
        """
        
        letterCache = collections.Counter(s) #frequency of letters
        freqPool = sorted(letterCache.items(),key=lambda x:-x[1]) #sort by occurances
        
        res = [] #output occurances
        for letter,count in freqPool:
            curr = [letter]*count
            res+=curr
        return "".join(res)
s=input()
print(frequencySort(s))