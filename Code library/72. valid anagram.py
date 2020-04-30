# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:24:14 2020

@author: Varsha
"""

def isAnagram(s,t):
        anagram = {}
        for char in s:
            anagram[char] = anagram.get(char, 0) + 1
        for char in t:
            if char not in anagram:
                return False 
            anagram[char] = anagram.get(char, 0) - 1
        for v in anagram.values():
            if v != 0:
                return False 
        return True
s=input()
t=input()
print(isAnagram(s,t))