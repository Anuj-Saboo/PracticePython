# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:21:25 2019

@author: Anuj Saboo
"""


def add():
    print("This is a prompt to add more user")
    name=input("Enter the name")
    dob=input("Enter birthday")
    read[name]=dob
    
    with open('info.json','w') as f:
        json.dump(read,f)
    
    with open('info.json','r') as f:
        write=json.load(f)
    
    print("Updated Dictionary is {}".format(write))

import json

with open('info.json','r') as f:
    read=json.load(f)
    
add()


