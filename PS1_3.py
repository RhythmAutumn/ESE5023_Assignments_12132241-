# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 21:29:34 2021

@author: zyq17713
"""

def Pascal_triangle(k):
    tri=[]
    for i in range(k):
        if i==0:
            tri.append([1])
        else:
            temp=[]
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(tri[i-1][j]+tri[i-1][j-1])
            tri.append(temp)

    s=str(tri[len(tri)-1])
    print(s.center(10*k))

Pascal_triangle(100)
Pascal_triangle(200)
