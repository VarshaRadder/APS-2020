# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:17:15 2020

@author: Varsha
"""
#In how many ways can a number be written as sum of 1 or more primes
def prime(n):
    lst=[]
    for i in range(2,n+1):
        t=True
        for j in range(2,i):
            if i%j==0:
                t=False
                break
        if t:
            lst.append(i)        
    return(lst)

m=int(input())  #number of test cases
for k in range(m):
    n=int(input())
    lst1=prime(n)
    lst3=[]
    for e in range(len(lst1)+1):
        lst2=[]
        lst2.append(1)
        for f in range(1,n+1):
            lst2.append(0)
        lst3.append(lst2)
    for e in range(1,len(lst1)+1):
        for f in range(1,n+1):
            lst3[e][f]=lst3[e-1][f]+lst3[e][f-lst1[e-1]]
    print(lst3[e][f])

