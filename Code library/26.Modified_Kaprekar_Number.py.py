# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 15:16:15 2020

@author: Varsha
"""
import math
import os
import random
import re
import sys
import math 


def kaprekarNumbers(p, q):
    kap=[1, 9, 45, 55, 99, 297, 703, 999, 2223 ,2728, 4950, 5050, 7272, 7777, 9999 ,17344, 22222,77778,82656,95121, 99999]
    flag=0
    a=list(range(p,q+1))
    for j in kap:
        if j in a:
            print(j,end=" ")
            flag=1
    if flag==0:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())
    kaprekarNumbers(p, q)
