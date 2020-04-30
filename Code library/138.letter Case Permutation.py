# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:09:19 2020

@author: Varsha
"""
def letterCasePermutation( S):

        running_result =[""]
        for idx in range(len(S)):
            new_result = []
            if S[idx].isdigit():
                for word in running_result:
                    new_result.append(word + S[idx])
            else:
                for word in running_result:
                    new_result.append(word + S[idx].upper())
                    new_result.append(word + S[idx].lower())
            running_result = new_result
        return running_result
S=input()
print(letterCasePermutation( S))