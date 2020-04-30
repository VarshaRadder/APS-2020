# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:29:23 2020

@author: Varsha
"""
def checkPerfectNumber(num):
		if num <= 1: return False
		res,sq=0,int(num**0.5)
		for i in range(2,sq+1):
			if num % i == 0:
				res += i + num//i
		res += 1
		return res == num

num=int(input())
print(checkPerfectNumber(num))