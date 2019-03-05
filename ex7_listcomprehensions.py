# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:46:52 2019

@author: Anuj Saboo
"""
import random
a = random.sample(range(10,50),10)
print(list(filter(lambda x: (x % 2==0) , a)))
