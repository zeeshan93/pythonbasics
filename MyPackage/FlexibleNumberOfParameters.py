'''
Created on 05-Jul-2016

@author: zeeshan
'''
def add_Number(*args):
    total = 0
    for a in args:
        total += a
    print(total)
    
add_Number(3)
add_Number(1,2,3)
add_Number(1,2,3,4,5)