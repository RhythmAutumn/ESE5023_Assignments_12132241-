# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:01:13 2021

@author: zyq17713
"""

import random
x=random.randint(1,100)
print("x="+str(x))

def Least_moves(x):
    n=0
    if x==1:
        n=0
    else:
        #For x>=2,x/2<=x-1
        while x!=1:
            if x%2==0:
                x=x/2
                n=n+1
            else:
                x=x-1
                n=n+1      
    return n
    
print("Least_moves("+str(x)+")="+str(Least_moves(x)))  
        
    
    