# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:49:05 2020

@author: Varsha
"""

def lengthOfLongestSubstring(s):
        d=dict()
        max=0
        if(len(s)==1):
            return ("1")
        for j in range (len(s)):
            for i in range(j,len(s)):
                if s[i] not in d:
                    d[s[i]]=1
                elif(s[i] in d):
                    l=len(d)
                    if(l>max):
                        max=l
                    d={}
                    break        
        return(max)
s=input()
print(lengthOfLongestSubstring(s))