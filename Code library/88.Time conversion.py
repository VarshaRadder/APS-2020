# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:44:36 2020

@author: Varsha
"""

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    ss=s.split(":")
    b=ss[2][2:]
    c=ss[2][0:2]
    ss.pop(2)   
    if b=='PM':
        if ss[0]!='12':
            a=str(12+int(ss[0]))
            ss.pop(0)
            ss.insert(0,a)
    if b =='AM':
      if ss[0]=='12':
        ss.pop(0)
        ss.insert(0,'00')
        print(ss[0])

    ss.insert(1,':')
    ss.insert(3,':')
    ss.insert(4,c)
    return ''.join(ss)

s = input()
print(timeConversion(s))

