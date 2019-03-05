# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:52:56 2019

@author: Anuj Saboo

"""

from collections import Counter
import json
with open('info.json','r') as f:
    data=json.load(f)

num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}
months=[]
for a,b in data.items():  #a becomes name and b becomes birthday
    month = int(b.split("/")[1])
    c=num_to_string[month]
    months.append(c)
print(Counter(months))
    