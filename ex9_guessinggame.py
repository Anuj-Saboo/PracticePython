# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:16:56 2019

@author: Anuj Saboo
"""

import random
d=0
while True:
    a=random.randint(1,10)     
    b=int(input("Enter a number: "))
    if(a<b):
        print("Number entered is Too High")
    elif(a>b):
        print("Number entered is Too Low")
    elif(a==b):
        print("Number entered is Equal")
    d=d+1
    c=input(print("Do you want to exit "))
    if c!='exit':
        continue
    else:
        break;
    
print("You took "+str(d)+" guesses")
