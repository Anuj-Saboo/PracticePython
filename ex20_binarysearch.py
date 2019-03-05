# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:35:32 2019

@author: Anuj Saboo
"""

def search(array,num):
    if num in array:
        print("Number exists")
    else:
        print("Number does not exist")
        
        
def binarysearch(array,num):
	first = 0
	last = len(array)-1
	found = False
	while first<=last and not found:
		mid = (first + last)//2
		if array[mid] == num:
			found = True
		else:
			if num < array[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
    
import random
array=sorted(random.sample(range(500),10))
print(array)
num=int(input("Enter a number"))
search(array,num)
print(binarysearch(array,num))

