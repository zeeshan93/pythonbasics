'''
Created on 05-Jul-2016

@author: zeeshan
'''
import urllib.request
import random

def download_image(url):
    name = random.randrange(1,100)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)
    
download_image("https://thenewboston.com/photos/users/2/original/21cb2a676d59d91335788ee8158e7ef0.jpg")