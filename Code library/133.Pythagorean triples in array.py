# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:45:27 2020

@author: Varsha
"""
import math  

def findTriplet(arr, n): 
  # Step1
  for i in range(n): 
    arr[i] = arr[i] * arr[i] 
  arr.sort() 

  # Step 2 and Step 3
  for i in range(n-1, 1, -1):   # fix a
    b = 0                       # fix b
    c = i - 1                   # fix c
    while (b < c): 
      if (arr[b] + arr[c] == arr[i]): 
        print("Triplet: ", math.sqrt(arr[b]),", ",math.sqrt(arr[c]),", ", math.sqrt(arr[i]))
        b+=1
        c-=1
      else: 
        if (arr[b] + arr[c] < arr[i]): 
          b = b + 1
        else: 
          c = c - 1

# Driver program to test above function */ 
arr = [3, 1, 4, 6, 5] 
n = len(arr) 
findTriplet(arr, n)
