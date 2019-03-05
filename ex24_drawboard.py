# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:26:29 2019

@author: Anuj Saboo
"""

def draw(num):
    for i in range(num):
        print("--- "*num)
        print("| | " * num)
    print("--- "*num)

num=int(input("Enter the size of the board "))
draw(num)