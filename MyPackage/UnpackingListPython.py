'''
Created on 12-Jul-2016

@author: zeeshan
'''
def drop_first_last(grades):
    first , *middle , last = grades
    average = sum(middle) / len(middle)
    print(average)
    
drop_first_last([1,2,3,4,5])
drop_first_last([1,2,3,4,5,6,7,8])
drop_first_last([1,2,3,4,5,8,9,75])
drop_first_last([1,2,3,4,5,12,12,15,14,54])