# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:29:25 2020

@author: Varsha
"""

def isStrobogrammatic( num):
        table, n = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}, len(num)
        for i in range((n >> 1) + 1):
            if num[i] not in table or table[num[i]] != num[n - i - 1]:
                return False
        return True
num=(input())
print(isStrobogrammatic( num))