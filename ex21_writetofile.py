# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:36:27 2019

@author: Anuj Saboo
"""


a='TESTSTRING1'
      
filename=input("Enter the name of the file")
filename=filename+'.txt'
with open(filename,'w') as open_file:
    open_file.write(a)