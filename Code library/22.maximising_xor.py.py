# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:16:15 2020

@author: Varsha
"""


def maximizingXor(l, r):
    a = l^r 
  
    b = 0
    while(a): 
      
        b += 1
        a >>= 1
    c, d = 0, 1
      
    while (b): 
      
        c += d 
        d <<= 1
        b -= 1
  
    return c 



l = int(input())
r = int(input())
print(maximizingXor(l, r))