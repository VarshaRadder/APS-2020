# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:45:48 2020

@author: Varsha
"""
def romanToInt(s):
        lst=list(s)
        sum1=0
        j=0
        while(j<len(lst)):
            #print(lst[j])
            if lst[j]=='C' and j+1!=len(lst):
                if (lst[j+1]=='D' or lst[j+1]=='M'):
                    sum1=sum1-100
                else:
                  sum1=sum1+100
            if lst[j]=='X' and j+1!=len(lst):
                if (lst[j+1]=='L' or lst[j+1]=='C') :
                    sum1=sum1-10
                else:
                  sum1=sum1+10
            if lst[j]=='I' and j+1!=len(lst):
                if (lst[j+1]=='V' or lst[j+1]=='X'):
                    sum1=sum1-1
                else:
                  sum1=sum1+1
            if lst[j]=='M' :
                sum1=sum1+1000
            if lst[j]=='D':
                sum1=sum1+500
            if lst[j]=='L':
                sum1=sum1+50
            if lst[j]=='V':
                sum1=sum1+5
            if lst[j]=='X' and j==len(lst)-1:
                sum1=sum1+10
            if lst[j]=='C'and j==len(lst)-1:
                sum1=sum1+100
            if lst[j]=='I' and j==len(lst)-1:
                sum1=sum1+1
            j+=1
        return(sum1)
s=input()
print(romanToInt(s))