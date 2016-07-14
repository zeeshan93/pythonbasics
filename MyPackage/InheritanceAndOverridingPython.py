'''
Created on 11-Jul-2016

@author: zeeshan
'''
class Parent():
    
    def print_last_name(self):
        print('Ahmed Khan')
        
class Child(Parent):
    
    def print_first_name(self):
        print('Zeeshan')
        
    def print_last_name(self):
        print('Khan')
        
zee = Child()
zee.print_first_name()
zee.print_last_name()