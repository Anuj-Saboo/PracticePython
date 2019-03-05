# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:48:21 2019

@author: Anuj Saboo

"""

counter_dict = {}
with open('nameslist.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)


#Below is for Extra question
counter_dict={}
with open('Training_01.txt','r') as f:
    line=f.readline()
    while line:
        line=line.strip()
        a=line.split('/')
        if a[2] in counter_dict:
            counter_dict[a[2]]=counter_dict[a[2]]+1
        else:
            counter_dict[a[2]]=1
        line=f.readline()

print(counter_dict)
            



