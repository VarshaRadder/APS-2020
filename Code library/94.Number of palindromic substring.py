# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:48:30 2020

@author: Varsha
"""

def countSubstrings(s):
        if not s:
            return 0
        n = len(s)
        s = list(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in reversed(range(n)):
            dp[i][i] = True
            res += 1
            for j in range(i + 1, n):
                if j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                if dp[i][j]:
                    res += 1
        return res
    
s=input()
print(countSubstrings(s))