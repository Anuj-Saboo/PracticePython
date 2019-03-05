# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:27:19 2019

@author: Anuj Saboo



def game(a,guess):
    print("_ " * len(a))
    while b!=a:
        for i range(len(a)):
            if a[i]==guess:
"""                
        
        

a=[]
with open('sowpods.txt','r') as p:
    line=p.readline().strip()
    while line:
        a.append(line)
        line=p.readline().strip()
    
import random
print(random.choice(a))

    

#guess=input("Enter a guess:")
#game(a,guess)
