# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:12:06 2019

@author: Anuj Saboo
"""

def listends(a):
    b=[]
    b=[a[0],a[-1]]
    return b


import random
a=random.sample(range(50),9)
print(a)
print(listends(a))