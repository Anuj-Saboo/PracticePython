# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:22:15 2019

@author: Anuj Saboo
"""
from bokeh.plotting import figure, show, output_file
from collections import Counter
import json
with open('scientist_birthdays.json','r') as f:
    data=json.load(f)

num_to_string = {
	1: "Jan",
	2: "Feb",
	3: "Mar", 
	4: "Apr",
	5: "May",
	6: "Jun",
	7: "Jul",
	8: "Aug",
	9: "Sep",
	10: "Oct",
	11: "Nov",
	12: "Dec"
}

months=[]
for a,b in data.items():  #a becomes name and b becomes birthday
    month = int(b.split("/")[0])
    c=num_to_string[month]
    months.append(c)
d=Counter(months)

x_categories=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

output_file("plot.html")
x = [a for a in d]   #You get each month as X
y = [d[a] for a in d] #You map counter[month] to get frequency in y

p = figure(x_range=x_categories)
p.vbar(x=months, top=y, width=0.5)


show(p)
