# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:06:53 2019

@author: Anuj Saboo
"""
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in range(len(a)):
    if a[i] in a[i+1:]:
        a[i]=0
    for j in range(len(b)):
        if(a[i]==b[j]):
            c.append(a[i])
print(c)

"""
#Option2: Using a function intersect

def intersect(a, b):
    return list(set(a) & set(b)) # the & is for intersection, which will take the common between the two

def main():
    #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(intersect(a, b))

#main()

#For Random List Generation

import random

a = random.sample(range(0,50),9) #generate 9 random numbers between 0 & 50
b = random.sample(range(0,50),11)
main()
