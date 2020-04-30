# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:45:38 2020

@author: Varsha
"""

def dayOfYear(date):
        y, m, d = (int(x) for x in date.split("-"))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        return sum(days[:(m-1)]) + d + (m > 2 and (y%4 == 0 and y%100 != 0 or y%400 == 0))
    
date=input()
print(dayOfYear(date))