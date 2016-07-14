'''
Created on 13-Jul-2016

@author: zeeshan
'''
income = [10,20,75]

def doubleMoney(dollars):
    return dollars * 2

newIncome = list(map(doubleMoney,income))
print(newIncome)