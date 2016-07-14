'''
Created on 13-Jul-2016

@author: zeeshan
'''
from operator import attrgetter

class User:
    
    def __init__(self,x,y):
        self.name = x
        self.userId = y
        
    def __repr__(self):
        return self.name +":"+str(self.userId)
    
users = [
         User("Zeeshan",100),
         User("Faizan",200),
         User("Atif",30),
         User("Shoiab",40)
         ]

for user in users:
    print(user)
    
print('---------------')

print("Sorted by Name")

print("Sort example: ")

print(sorted(users,key=attrgetter('name')))

for user in sorted(users,key=attrgetter('name')):
    print(user)
    
print('---------------')

print("Sorted by user id")

for user in sorted(users,key=attrgetter('userId')):
    print(user)