'''
Created on 12-Jul-2016

@author: zeeshan
'''
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a',{'class':'title text-semibold'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            #print(each_word)
            word_list.append(each_word)
            clean_up_word(word_list)
            
            
def clean_up_word(word_list):
    clean_word_list = []
    symbols = "!@#$%^&*()_+{}|:~`\"<>?-=[]\;',./"
    for word in word_list:
        for i in range(0,len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word) > 0:
            #print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)
            
            
            
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    '''
        key=operator.itemgetter(1) does not indicate key in the dictionary. 
        operator.itemgetter(0) indicate sort by key.
        operator.itemgetter(1) indicate sort by value.
    '''        
    for key, value in sorted(word_count.items(),key=operator.itemgetter(1)):
        print(key , value)
    
    
start('https://thenewboston.com/forum/#')