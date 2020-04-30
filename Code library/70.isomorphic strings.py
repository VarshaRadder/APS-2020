# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:35:38 2020

@author: Varsha
"""

from collections import Counter
def isIsomorphic(s,t):
        col=Counter(s)
        col1=Counter(t)

        if s==t:
            return True
        st=list(s)
        tt=list(t)
        s=list(s)
        t=list(t)
        for i,k in col.items():
            for j,m in col1.items():
                if k==m:

                    for p in range(len(s)):
                        if i==s[p]:
                            s[p]=j
                    for p in range(len(t)):
                        if j==t[p]:
                            t[p]=i   
        if st==t and tt==s:
            return True
        else:
            return False
s=input()
t=input()
print(isIsomorphic(s,t))