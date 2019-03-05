# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:14:02 2019

@author: Anuj Saboo
"""

def findmax(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(str(num1)+" is greatest")
    elif num2>num3 and num2>num1:
        print(str(num2)+" is greatest")
    else:
        print(str(num3)+" is greatest")



num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
findmax(num1,num2,num3)

"""

Method 2 by sorthing list and returning last element

def findmax(num1,num2,num3):
   a=[num1,num2,num3]
   a.sort()
   print(str(a[2])+" is largest")


num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
findmax(num1,num2,num3)

"""