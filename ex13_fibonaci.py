# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:15:52 2019

@author: Anuj Saboo
"""
def fibo(num):
    
    a=[1,1]
    if num==1:
        return([1])
    elif num==2:
        return([1,1])
    else:
        for i in range(2,num):
            a.append(a[i-1]+a[i-2])
    return(a)
        

num=int(input("Enter the number of fibonaci numbers to generate: "))
print(fibo(num))



