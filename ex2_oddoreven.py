# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:02:59 2019

@author: Anuj Saboo
"""

num1=int(input("Enter a number: "))
check=int(input("Enter a divisor: "))
if(num1%2==0):
    print("Number is even")
    if(num1%4==0):
        print("Number is multiple of 4")
      
else:
    print("Number is odd")
    
if(num1%check==0):
    print("Number divisible by "+str(check))
else:
    print("Number not divisible by "+str(check))