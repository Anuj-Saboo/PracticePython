# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:15:46 2019

@author: Anuj Saboo
"""

word="EVAPORATE"
word=list(word)
guessed='_'*len(word)
guessed=list(guessed)
used=[] #lIST TO STORE WORDS BEING GUESSED TO TELL USER NOT TO REPEAT SAME WORD
while '_' in guessed:
    print(guessed)
    guess=input("Enter a guess: ")
    if guess not in used:
        used.append(guess)
        while guess in word:  #WHILE FOR MULTIPLE OCCURENCES OF SAME WORD
            index=word.index(guess)
            guessed[index]=guess
            word[index]='_'  
    else:
        print("Word has been guessed, please try again")        
    
print(guessed)

    
