# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:52:56 2020

@author: Varsha
"""
def climbStairs(n):
        def factorial(n):
            res =1
            for i in range(1,n+1):
                res = res*i
            return res
			
        if n <=3:
            return n
        else:
            sum = 0
            for i in range(n//2+1):
                sum += factorial(n-i)/(factorial(i)*factorial(n-2*i))
            return int(sum)
n=int(input())
print(climbStairs(n))