# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:37:10 2019

@author: Anuj Saboo
"""

def game(tries):
        b=0
        c=0
        tries=tries+1
        comp=[]
        for i in range(4):
            comp.append(random.randint(0,9))
        user=list(input("Enter a 4 digit number: "))
        for i in range(4):
            if int(user[i])==comp[i]:
                c=c+1
            elif int(user[i]) in comp:
                b=b+1
        
        print("Number of cows= " +str(c))
        print("Number of bulls= " +str(b))
        if c==4:
            print("Number of tries: "+str(tries))
        else:
            game(tries)
            
import random
tries=0    
game(tries)

