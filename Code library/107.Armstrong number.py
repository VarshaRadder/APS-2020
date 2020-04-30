# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:30:48 2020

@author: Varsha
"""
num = int(input("Enter a number: "))
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
