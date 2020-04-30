# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:47:35 2020

@author: Varsha
"""

def wordPattern(pattern,str):
        pattern_dict = {}
        str_dict = {}
        str_word = str.split()
        if len(pattern) != len(str_word):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = i
                print(pattern_dict[pattern[i]])
            if str_word[i] not in str_dict:
                str_dict[str_word[i]] = i
                #print(str_dict[str_word[i]])
        for i in range(len(pattern)):
            if pattern_dict[pattern[i]] != str_dict[str_word[i]]:
                return False
        return True
pattern=input()
str=input()
print(wordPattern(pattern,str))