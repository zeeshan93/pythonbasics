'''
Created on 13-Jul-2016

@author: zeeshan
'''
stocks = {
          "GOOG":574.62,
          "AAPL":500.4,
          "FB":455.65,
          "F":21.00,
          "MSFT":496.45
          }

minPrice = min(zip(stocks.values(),stocks.keys()))
print(minPrice)