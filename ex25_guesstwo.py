# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:34:20 2019

@author: Anuj Saboo
"""

def guess():
    front = 0
    
    last = 100
    # j is the highest number in range of possible guesses
    mid = 50
    # m is the middle number in range of possible guesses
    counter = 1
    # counter is the number of guesses take.
    print("Please guess a number")
    condition = input("Is your guess " + str(mid) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
    while condition != 1:
        counter += 1
        if condition == 0:
            front = mid + 1
        elif condition == 2:
            last = mid - 1
        mid = (front + last) // 2
        condition = input("Is your guess " + str(mid) + "?")
    print("It took" , counter , "times to guess your number")
guess()