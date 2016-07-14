'''
Created on 06-Jul-2016

@author: zeeshan
'''
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1;
    while page <=max_pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll('a', {'class':'item-name'}):
            href = link.get('href')
            print(href)
        page +=1;

trade_spider(1)