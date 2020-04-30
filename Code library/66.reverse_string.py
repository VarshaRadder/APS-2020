# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:11:27 2020

@author: Varsha
"""
def reverseWords(s):
        # s = "a good   example"
        res =''
        for word in reversed(s.split()):
            res = res + ' ' + word
        return res.strip()
s=input()
print(reverseWords(s))
