# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:31:26 2020

@author: Varsha
"""
import math
def countPrimes(n):
        if n==0 or n==1:
            return 0
        prime = [True]*(n)
        prime[0] = False
        prime[1] = False
        for i in range(2,int(math.sqrt(n)+1)):
            if prime[i]==True:
                j=2
                while i*j<n:
                    prime[i*j]=False
                    j+=1
        return sum(prime)
n=int(input())
print(countPrimes(n))
