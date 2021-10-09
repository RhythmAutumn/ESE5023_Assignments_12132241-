# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:28:23 2021

@author: zyq17713
"""

#5.1 The space between each number can be filled with "+","-" or "",递归思想
import random
x=random.randint(1,100)
print("x="+str(x))
    
def fun(x, digit, aa: str):
    if len(digit) == 1:
        for i in range(len(digit)):
            a = digit[i]
            b = digit[:]
            b.pop(i)
            temps = str(a)
            aa = aa + temps
            if eval(aa) == x:
                print(aa + "=" + str(x))
    else:
        for i in range(len(digit)):
            a = digit[i]
            b = digit[:]
            b.pop(i)
            temps = str(a)
            aa = aa + temps
            fun(x, b, aa + '+')
            fun(x, b, aa + '-')
            fun(x, b, aa + '')
            return True

def Find_expression(x):
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return fun(x,digit,'')

result=Find_expression(x)


#5.2 
def Find_count(x):
    sym = ['+','-','']
    s=''
    count=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for n in range(3):
                            for o in range(3):
                                for p in range(3):
                                    digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                                    digit.insert(1,sym[i])
                                    digit.insert(3,sym[j])
                                    digit.insert(5,sym[k])
                                    digit.insert(7,sym[l])
                                    digit.insert(9,sym[m])
                                    digit.insert(11,sym[n])
                                    digit.insert(13,sym[o])
                                    digit.insert(15,sym[p])
                                    ex=s.join(digit)
                                    if eval(ex) == x:
                                        count=count+1
                                        continue
    return count

Total_solutions=[]

for i in range(100):
    temp=Find_count(i+1)
    Total_solutions.append(temp)
print(Total_solutions)
    
a=max(Total_solutions)
b=min(Total_solutions)
for j in range(100):
    if Total_solutions[j] == a:
        print("i="+str(j+1)+" can yield the maximum number "+str(a)+" of Total_solutions.")
    if Total_solutions[j] == b:
        print("i="+str(j+1)+" can yield the minimum number "+str(b)+" of Total_solutions.")
