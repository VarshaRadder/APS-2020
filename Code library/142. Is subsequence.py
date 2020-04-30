# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:49:19 2020

@author: Varsha
"""
'''
check if s is subsequence of t
'''


def isSubsequence(s,t):
        for i in s:
            if i in t: t = t[t.index(i) +1:]
            else: return False
        else: return True
s=input()
t=input()
print(isSubsequence(s,t))