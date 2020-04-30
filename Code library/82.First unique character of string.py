# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:28:58 2020

@author: Varsha
"""

def firstUniqChar(s):
        s1 =s
        while s != "":
            if s[0] not in s[1:]:
                return s1.index(s[0])
            s = "".join(s.split(s[0]))
        return -1
s=input()
if firstUniqChar(s)==-1:
    print("NO unique character")
else:
    print(s[firstUniqChar(s)])