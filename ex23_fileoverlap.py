# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:10:08 2019

@author: Anuj Saboo
"""
a=[]

with open('primenumbers.txt','r') as p:
    with open('happynumbers.txt','r') as h:
        prime=p.readlines()
        happy=h.readlines()
        for x in prime:
            for y in happy:
                if x==y:
                    a.append(x.rstrip())
        
print(a)