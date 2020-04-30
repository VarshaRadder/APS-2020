# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:15:59 2020

@author: varsha
"""

def isHappy(n):
        def sum1(n):
            rem=0
            sum2=0
            while(n>0):
                rem=n%10
                sum2+=(rem*rem)
                n=n//10
            return sum2
        while(n!=1 and n!=4):
            n=sum1(n)
        if n==1:
            return True
        else:
            return False
n=int(input())
print(isHappy(n))