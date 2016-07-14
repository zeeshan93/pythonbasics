'''
Created on 12-Jul-2016

@author: zeeshan
'''
myDictionary = {
                "GOOG":593.45,
                "FB":456.25,
                "YHOO":125.25,
                "AMZN":500.63,
                "AAPL":555.45
                }

print(min(zip(myDictionary.values(),myDictionary.keys())))
print(max(zip(myDictionary.values(),myDictionary.keys())))
print(sorted(zip(myDictionary.values(),myDictionary.keys())))