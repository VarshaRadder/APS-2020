# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:54:20 2020

@author: Varsha
"""

lower = 100
upper = 1000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)