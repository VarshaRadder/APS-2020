# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:24:51 2020

@author: Varsha
"""
#Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.

def camelMatch(queries,pattern):
        def isMatch(word, pat):
            i, j = 0, 0
            while j < len(word) and i < len(pat):
                if word[j] == pat[i]:
                    i += 1
                elif word[j].isupper(): 
                    return False                                 
                j += 1
            return i == len(pat) and not any(ch.isupper() for ch in word[j:])                                
        return [isMatch(word, pattern) for word in queries]
queries=list(input().split())
pattern=input()
print(camelMatch(queries,pattern))