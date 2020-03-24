# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:11:35 2020

@author: Varsha
"""

def a(x1, y1, x2, y2, x3, y3):   
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 
  
def check(x1, y1, x2, y2, x3, y3, x, y): 
    b1 = a(x1, y1, x2, y2, x3, y3) 
    b2 = a(x, y, x2, y2, x3, y3)  
    b3 = a(x1, y1, x, y, x3, y3) 
    b4 = a(x1, y1, x2, y2, x, y) 
    if(b1==b2+b3+b4): 
        return True
    else: 
        return False
n=int(input())  # n: number of triangles
lst2=[0]
for i in range(n):
    lst=list(map(int,input().split())) #6 space separated integers representing a triangle.
    if (check(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],0,0)): 
        lst2[0]+=1
print("The number of triangles for which the interior contains the origin:")
print(lst2[0]) 
