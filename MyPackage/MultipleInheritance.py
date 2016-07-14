'''
Created on 12-Jul-2016

@author: zeeshan
'''
class Mario():
    def move(self):
        print('I can move')
        
class Shroom():
    def eat_shroom(self):
        print('I grow big')
        
class BigMario(Mario,Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()