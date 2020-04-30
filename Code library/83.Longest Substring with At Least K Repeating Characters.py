# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:32:03 2020

@author: Varsha
"""

def longestSubstring(s,k):
        if not s:
            return 0
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        # fill diagonal first
        for i in range(len(dp)):
            table = {}
            table[s[i]] = 1
            if k == 1:
                dp[i][i] = (table, 1)
            else:
                dp[i][i] = (table, 0)
        # fill the rest of the valid cells
        for i in range(len(dp)):
            for j in range(i):
                # take table from above
                table = dp[i-1][j][0]
                # add the new character
                if s[i] in table:
                    table[s[i]] += 1
                else:
                    table[s[i]] = 1
                # check for longer substring
                k_true = True
                for key in table:
                    if table[key] < k:
                        k_true = False
                if k_true:
                    dp[i][j] = (table, max(len(s[j:i+1]), dp[i-1][j][1]))
                else:
                    dp[i][j] = (table, dp[i-1][j][1])
        # take the max from last line
        longest = 0
        for tup in dp[-1]:
            longest = max(longest, tup[1])
        return longest
s=input()
k=int(input())
print(longestSubstring(s,k))

