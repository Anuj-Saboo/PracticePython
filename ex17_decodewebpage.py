# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:23:16 2019

@author: Anuj Saboo
"""

import requests
from bs4 import BeautifulSoup
url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
for link in soup.find_all('h2'):
    print(link)
    