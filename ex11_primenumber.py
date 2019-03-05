# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:06:52 2019

@author: Anuj Saboo
"""

def prime(num):
    if num==1:
        return True
    else:
        for i in range(2,num):
            if(num%i==0):
                return False
            else:
                return True
        


num=int(input("Enter a number: "))
if (prime(num)):
    print("Number is Prime")
else:
    print("Number is not Prime")
    