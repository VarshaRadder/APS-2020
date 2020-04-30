# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:10:36 2020

@author: Varsha
"""

for i in range(int(input())):
    a=input()
    if((len(a))%2 != 0):
        if(sorted(a[:int(len(a)/2)]) == sorted(a[int(len(a)/2)+1:])):
            print('YES')
        else:
            print('NO')
    else:
        if(sorted(a[:int(len(a)/2)]) == sorted(a[int(len(a)/2):])):
            print('YES')
        else:
            print('NO')