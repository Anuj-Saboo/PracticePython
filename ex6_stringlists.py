# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:33:20 2019

@author: Anuj Saboo
"""

str=input("Enter a string: ")
a=""
a=str[::-1]
if a==str:
    print("String is a palindrome")
else:
    print("String is not a palindrome")