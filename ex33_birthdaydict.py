# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:59:56 2019

@author: Anuj Saboo
"""

birthday_dict={'Anuj':'17/12/1991','Ram':'1/1/2001','Sam':'2/1/2002'}
print("Welcome to the Birthday Dictionary")
print("We know the birthdays of:")
print('\n'.join(birthday_dict.keys()))
name=input("Whose birthday do you want to lookup: ")
if name not in birthday_dict:
    print("{} is not in dictionary".format(name))
else:
    #print(name+"'s birthday is on "+birthday_dict[name])
    print("{}'s birthday is on {}".format(name,birthday_dict[name]))
    