'''
Created on 04-Jul-2016

@author: zeeshan
'''
def allowed_to_date(dude_age):
    girls_age = dude_age/2 + 7;
    return girls_age

for x in range(15,60):
    girls_age = allowed_to_date(x)
    print("Dude is ", x ," years old and he/she can date a girl with age ", girls_age ," or older")
    