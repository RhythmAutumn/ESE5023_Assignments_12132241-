# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:33:00 2021

@author: zyq17713
"""

import numpy as np
M1=np.mat(np.random.randint(0,51,[5,10]))
M2=np.mat(np.random.randint(0,51,[10,5]))
print(M1)
print(M2)

def Matrix_multip(M1,M2):
    M3=[]
    for i in range(len(M1)):
        temp=[]
        for j in range(len(M2[0].T)):
            s=0
            for k in range(len(M2)):
                s+=(M1[i,k])*(M2[k,j])
            temp.append(s)
        M3.append(temp)
    return np.mat(M3)

print(Matrix_multip(M1,M2))

print(M1*M2)#To prove the accuracy of the function
