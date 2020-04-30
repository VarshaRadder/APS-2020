# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:53:49 2020

@author:Varsha
"""
def toHex(num):
        s = bin(num & 0xffffffff).replace("0b", "")
        #print(s)
        res = ""
        for i in range(len(s), -1, -4):
            if s[0:i] and len(s[0:i]) < 4:

                res = str(int(s[0:i], 2)) + res
            elif len(s[i-4:i]) > 0:
                #print(s[i-4:i])

                a = int(s[i-4:i], 2)
                if a > 9:

                    c = chr(97 + a - 10)
                else:
                    c = str(a)
                res = c + res
        return res
num=int(input())
print(toHex(num))