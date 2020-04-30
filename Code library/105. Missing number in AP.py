# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:58:50 2020

@author: Varsha
"""

import sys 
 
def findMissingUtil(arr, low, high, diff):  
 
    if (high <= low):  
        return sys.maxsize;  
 
    mid = int(low + (high - low) / 2);  

    if (arr[mid + 1] - arr[mid] != diff):  
        return (arr[mid] + diff);  
 
    if (mid > 0 and arr[mid] - 
                    arr[mid - 1] != diff):  
        return (arr[mid - 1] + diff);  

    if (arr[mid] == arr[0] + mid * diff):  
        return findMissingUtil(arr, mid + 1, 
                                high, diff);  

    return findMissingUtil(arr, low, 
                           mid - 1, diff);  

def findMissing(arr, n):  
  
    diff = int((arr[n - 1] - arr[0]) / n);  
 
    return findMissingUtil(arr, 0, n - 1, diff);  

arr = [2, 4, 8, 10, 12, 14];  
n = len(arr);  
print("The missing element is", 
          findMissing(arr, n)); 