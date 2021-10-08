# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:29:54 2021

@author: zyq17713
"""
import random

def Print_values():
    a=random.random()
    b=random.random()
    c=random.random()
    if (a>b):
        if (b>c):
            return a,b,c
        elif (a>c):
            return a,c,b
        else:
            return c,a,b
    elif (b>c):
        if (a>c):
            return None
        else:
            return None
    else:
        return c,b,a
        
print(Print_values())
            