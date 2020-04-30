# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:19:48 2020

@author: Varsha
"""

def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input())
num2 = int(input())

print("The L.C.M. is", compute_lcm(num1, num2))