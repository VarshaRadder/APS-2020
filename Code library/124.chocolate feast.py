# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:54:02 2020

@author: Varsha
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    cost=n//c
    temp=cost
    while temp>=m:
        x=temp//m
        cost+=x
        temp=x+(temp%m)
    return cost


t = int(input())

for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)
        print(result)

