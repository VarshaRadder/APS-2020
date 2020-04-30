# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:54:20 2020

@author: Varsha
"""

def uncommonFromSentences(a,b):
                                lt=list(a.split()+b.split())
                                test,res={},[]
                                for i in lt:
                                        if i not in test:
                                              test[i]=1
                                        else: 
                                              test[i]+=1
                                for k,v in test.items():
                                      if v==1:
                                             res.append(k)
                                return res
A=input()
B=input()
print( uncommonFromSentences(A,B))