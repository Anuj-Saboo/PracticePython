# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:10:36 2019

@author: Anuj Saboo
"""
#Option1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(len(a)):
    if a[i]<5:
        print(a[i])
    
#Option2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list(filter(lambda x: (x < 5) , a)))        

#Option3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=int(input("Enter a number: "))
print(list(filter(lambda x: (x<b),a)))
        