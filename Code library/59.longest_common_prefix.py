# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:53:24 2020

@author: Varsha
"""
def longestCommonPrefix(strs):
        flag=0
        lst=[]
        if len(strs)==0:
            return ""
        minle=len(strs[0])
        for j in range(len(strs)):
            if minle>len(strs[j]):
                minle=len(strs[j])
        k=0
        for k in range(minle):
            flag=0
            for j in range(1,len(strs)):
                if strs[0][k]==strs[j][k]:
                    flag+=1
                
            if flag==len(strs)-(1):
                lst.append(strs[0][k])
                flag=0
        if len(lst)>0:
            for j in range(len(strs)):
                if lst[0]!=strs[j][0]:
                    return("")
            return ''.join(lst)
        else:
            return ""
strs=list(input().split())
print(longestCommonPrefix(strs))
