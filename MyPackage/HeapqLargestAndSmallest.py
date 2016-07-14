'''
Created on 13-Jul-2016

@author: zeeshan
'''
import heapq

items = [1,2,3,4,5,6,7,8]
print(heapq.nlargest(1, items))

stocks = [
          {'tickle':'GOOG','price':567},
          {'tickle':'AAPL','price':500},
          {'tickle':'FB','price':512},
          {'tickle':'MSFT','price':400},
          {'tickle':'AMZN','price':300}        
          ]

print(heapq.nsmallest(1, stocks, key=lambda stocks:stocks['price']))