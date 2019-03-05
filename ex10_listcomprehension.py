# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 07:55:02 2019

@author: Anuj Saboo
"""

def intersect(a,b):
    return (set(a) & set(b))

def comp(a,b):
    return(set(x for x in a if x in b))
    

import random
a=random.sample(range(50),9)
b=random.sample(range(50),11)
print("List 1 is "+ str(a))
print("List 2 is "+ str(b))
print(intersect(a,b))
print(comp(a,b))