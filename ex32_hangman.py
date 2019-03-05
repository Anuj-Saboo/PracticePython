# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:30:06 2019

@author: Anuj Saboo
"""

def hangman():
    t=0
    a=[]
    with open('sowpods.txt','r') as p:
        line=p.readline().strip()
        while line:
            a.append(line)
            line=p.readline().strip()
    
    import random
    word=random.choice(a)

    word=list(word)
    guessed='_'*len(word)
    guessed=list(guessed) 
    used=set()  #Using set instead of a list is faster. Here storing used words to alert user
    while '_' in guessed and t < 6:
        print(guessed)
        guess=input("Enter a guess: ")
        if guess not in used:
            used.add(guess)
            if guess not in word:
                t=t+1
            else:
                while guess in word:  #WHILE FOR MULTIPLE OCCURENCES OF SAME WORD
                    index=word.index(guess)
                    guessed[index]=guess
                    word[index]='_'            
        else:
            print("Word has been guessed, please try again")        
    
    print(guessed)

    print("Game Over.")

hangman()



