# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:57:31 2023

@author: AlperB
"""
import string
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

class MedLineScraper:
    def __init__ (self):
        self.base_url="https://www.volksliederarchiv.de/a-z/buchstabe-"
        self.lyrics_links= set()
    #abcd kategoriler    
    def get_categories(self):
        #letters = string.ascii_lowercase
        letters= "abcdefghijklmnopqrstuvwz"
        result= list (map(lambda letter: self.base_url+letter,letters))
        return result
    
    #kaynağı alıyoruz
    def get_source (self, url):
        r= requests.get(url)
        if r.status_code==200:
            return BeautifulSoup(r.content,"lxml")    
        return False 
    
    #linkleri alıyoruz
    def get_lyrics_links(self, source):
       lyrics_elements=source.find("div",attrs={"class":"letter-group"}).find_all("li")
       lyrics_links= list(map(lambda lyrics:lyrics.find("a").get("href"),lyrics_elements))
       return lyrics_links
   
    #bütün linklerin hepsini alıyoruz 
    def find_all_lyrics_links(self):
        #categories= self.get_categories()
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
'https://www.volksliederarchiv.de/a-z/buchstabe-z','https://www.volksliederarchiv.de/a-z/buchstabe-a/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-a/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-a/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-a/page/5/',
'https://www.volksliederarchiv.de/a-z/buchstabe-a/page/6/',
'https://www.volksliederarchiv.de/a-z/buchstabe-a/page/7/',
'https://www.volksliederarchiv.de/a-z/buchstabe-a/page/8/',
'https://www.volksliederarchiv.de/a-z/buchstabe-b/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-b/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-b/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/5/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/6/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/7/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/8/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/9/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/10/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/11/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/12/',
'https://www.volksliederarchiv.de/a-z/buchstabe-d/page/13/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/5/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/6/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/7/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/8/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/9/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/10/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/11/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/12/',
'https://www.volksliederarchiv.de/a-z/buchstabe-e/page/13/',
'https://www.volksliederarchiv.de/a-z/buchstabe-f/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-f/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-f/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-g/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-g/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-g/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-h/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-h/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-h/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-h/page/5/',
'https://www.volksliederarchiv.de/a-z/buchstabe-h/page/6/',
'https://www.volksliederarchiv.de/a-z/buchstabe-h/page/7/',
'https://www.volksliederarchiv.de/a-z/buchstabe-j/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-k/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-k/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-l/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-l/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-m/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-m/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-m/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-m/page/5/',
'https://www.volksliederarchiv.de/a-z/buchstabe-n/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-n/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-n/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-o/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-o/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-r/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-s/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-s/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-s/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-s/page/5/',
'https://www.volksliederarchiv.de/a-z/buchstabe-s/page/6/',
'https://www.volksliederarchiv.de/a-z/buchstabe-s/page/7/',
'https://www.volksliederarchiv.de/a-z/buchstabe-s/page/8/',
'https://www.volksliederarchiv.de/a-z/buchstabe-t/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-u/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-u/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-v/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-v/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/2/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/3/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/4/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/5/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/6/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/7/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/8/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/9/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/10/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/11/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/12/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/13/',
'https://www.volksliederarchiv.de/a-z/buchstabe-w/page/14/',
'https://www.volksliederarchiv.de/a-z/buchstabe-z/page/2/']
        bar=tqdm(categories,unit="category link")
        for category_link in bar:
            bar.set_description(category_link)
            category_source = self.get_source(category_link)
            result=self.get_lyrics_links(category_source)
            print(result)
            self.lyrics_links=self.lyrics_links.union(result)
        return self.lyrics_links
     
        #şarkının ismini çekme   
    def get_name(self, source):
        try: 
            text=source.find("title").text
            return text
        except Exception:
            return None 
        
        #şarkının temasını çekme
    def get_thema(self, source):
        try: 
            lyrics_elements=source.find("div",attrs={"id":"orange"}).find("p").find_all("span")[2].text
            #lyrics_thema= list(map(lambda lyrics:lyrics.find("span"),lyrics_elements))
            return lyrics_elements
        except Exception:
            return None        

    #texti alma    
    def get_text(self, source):
        lyrics_text=""   
        try:
            for i in source.find("div",attrs={"class":"entry-content"}).find_all("p"):
                lyrics_text=lyrics_text+i.get_text()
            return lyrics_text
        except Exception:
            None
    #main fonksiyon     
    def scrape_lyrics(self):
        result=list()
        links=list(self.find_all_lyrics_links())
        bar= tqdm(links, unit="Lyrics Links")
        #i=0
        for link in bar:
         #   if i ==20:
          #      break 
            bar.set_description(link)
            lyrics_source= self.get_source(link)
            name=self.get_name(lyrics_source)
            thema=self.get_thema(lyrics_source)
            text=self.get_text(lyrics_source)
            result.append(dict(
                    name=name,
                    url=link,
                    thema=thema,
                    text=text))
           # i +=1
        return result
    #json dosyasına yazma
    def write_as_json(self, data):
        with open ("result2.json", "w") as f:
            f.write(json.dumps(data, indent=2))
            
#ana fonksiyon
if __name__=='__main__':
    scraper = MedLineScraper()
    data= scraper.scrape_lyrics()
    scraper.write_as_json(data)