# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:01:14 2020

@author: Varsha
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0    
    if any(i.isdigit() for i in password)==False:
        count+=1
    if any(i.islower() for i in password)==False:
        count+=1
    if any(i.isupper() for i in password)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in password)==False:
        count+=1
    return max(count,6-n)


n = int(input())

password = input()

answer = minimumNumber(n, password)
print(answer)

