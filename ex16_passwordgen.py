# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:47:27 2019

@author: Anuj Saboo
"""


def genpass():
    n=int(input("Enter the length of the password: "))
    pop=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    return(''.join(random.sample((pop),n)))

import random
import string

print(genpass())

"""

Alternate Method without using string built in functions

import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print p

"""