# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 10:39:37 2023

@author: AlperB
"""

import requests #!pip install requests
from bs4 import BeautifulSoup #!pip install beautifulsoup4
import pandas as pd
import string
from tqdm import tqdm
import json

categories=['https://www.volksliederarchiv.de/a-z/buchstabe-a',
'https://www.volksliederarchiv.de/a-z/buchstabe-b',
'https://www.volksliederarchiv.de/a-z/buchstabe-c',
'https://www.volksliederarchiv.de/a-z/buchstabe-d',
'https://www.volksliederarchiv.de/a-z/buchstabe-e',
'https://www.volksliederarchiv.de/a-z/buchstabe-f',
'https://www.volksliederarchiv.de/a-z/buchstabe-g',
'https://www.volksliederarchiv.de/a-z/buchstabe-h',
'https://www.volksliederarchiv.de/a-z/buchstabe-i',
'https://www.volksliederarchiv.de/a-z/buchstabe-j',
'https://www.volksliederarchiv.de/a-z/buchstabe-k',
'https://www.volksliederarchiv.de/a-z/buchstabe-l',
'https://www.volksliederarchiv.de/a-z/buchstabe-m',
'https://www.volksliederarchiv.de/a-z/buchstabe-n',
'https://www.volksliederarchiv.de/a-z/buchstabe-o',
'https://www.volksliederarchiv.de/a-z/buchstabe-p',
'https://www.volksliederarchiv.de/a-z/buchstabe-q',
'https://www.volksliederarchiv.de/a-z/buchstabe-r',
'https://www.volksliederarchiv.de/a-z/buchstabe-s',
'https://www.volksliederarchiv.de/a-z/buchstabe-t',
'https://www.volksliederarchiv.de/a-z/buchstabe-u',
'https://www.volksliederarchiv.de/a-z/buchstabe-v',
'https://www.volksliederarchiv.de/a-z/buchstabe-w',
'https://www.volksliederarchiv.de/a-z/buchstabe-z']

def get_soup(TARGET_URL):
    page = requests.get(TARGET_URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


page_urls=[] 
for alp in categories:
    soup = get_soup(alp)

    pages = []
    try: 
        for k in soup.find_all('a', attrs={'class':'inactive'}):
            pages.append(k['href'])
            son_sayfa=int(pages[-1][-2])
        for i in range(2,son_sayfa+1):
            liste=alp+"/page/"+str(i)+"/"
            page_urls.append(liste)
                
    except Exception:
        None
    
print(page_urls)
#letters= "abcdefghijklmnopqrstuvwz"

