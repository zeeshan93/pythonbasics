'''
Created on 11-Jul-2016

@author: zeeshan
'''
class Girl:
    
    gender = 'Female'
    
    def __init__(self,name):
        self.name = name
    
p = Girl('Pooja Kaushik')
print(p.gender)
print(p.name)