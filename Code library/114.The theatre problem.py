# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:38:13 2020

@author: Varsha
"""


def cc(lst9):
    lst9.sort(reverse=True)
    y=0
    am=0
    lst6=[100,75,50,25]
    for u in range(len(lst9)):
        if lst9[u]==0:
          am=am-100
        else:
          am=am+(lst9[u]*lst6[y])
          y+=1
    return am
def se(pp, qq):
    if len(pp) == 1:
        qq.insert(len(qq), pp)
    else:
        for l in range(0,len(pp)):
            oo = pp[l]
            kk = [pp[m] for m in range(0,len(pp)) if m!= l]
            hh= []
            se(kk, hh)
            for rr in hh:
                ww = [oo] + rr
                qq.insert(len(qq), ww)
n=int(input())
import sys
lst7=[]
for i in range(n):
  p=int(input())
  lst1=[0]*4
  lst2=[0]*4
  lst3=[0]*4
  lst4=[0]*4
  for j in range(p):
    lst=input().split()
    if lst[1]=='12':
      lst1[abs(65-ord(lst[0]))]+=1
    if lst[1]=='3':
      lst2[abs(65-ord(lst[0]))]+=1     
    if lst[1]=='6':
      lst3[abs(65-ord(lst[0]))]+=1
    if lst[1]=='9':
      lst4[abs(65-ord(lst[0]))]+=1    
  lst=[]
  lst.append(lst1)
  lst.append(lst2)
  lst.append(lst3)
  lst.append(lst4)
  #print(lst)
  qq= []
  qq= []
  se(range(len(lst)),qq)
  lst8=[]
  lst10=[]
  lst9=[]
  for v in qq:
    cost = []
    for y, z in enumerate(v):
        cost.append(lst[y][z])
    lst8.append(cost)
  for g in range(len(lst8)):
      lst10.append(cc(lst8[g]))
  print(max(lst10))
  lst7.append(max(lst10))
print(sum(lst7))