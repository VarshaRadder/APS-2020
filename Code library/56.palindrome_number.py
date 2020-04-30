# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:37:53 2020

@author: Varsha
"""

def isPalindrome(x):
        result = 0
        remaining = abs(x)
        while remaining:
            result = result * 10 + remaining % 10
            remaining //= 10
    
        if result == x:
            return True
        else:
            return False
num=int(input())
print(isPalindrome(num))