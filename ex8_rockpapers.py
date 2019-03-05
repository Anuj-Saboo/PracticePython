# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:07:15 2019

@author: Anuj Saboo
"""
while True:
    play1=input("Enter first: ")
    play2=input("Enter second: ")
    if play1==play2:
        print("Cannot be same")
    elif play1=='rock' and play2=='scissors' or play1=='scissors' and play2=='paper' or play1=='paper' and play2=='rock':
        print("Player 1 wins")
    else:
        print("Player 2 wins")

    a=input("Do you want to play a new game? ")
    if a=='y':
        continue
    else:
        break

#not accounting for mistype during play