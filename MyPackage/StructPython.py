'''
Created on 12-Jul-2016

@author: zeeshan
'''
from struct import *

packedData = pack('iif', 6, 19, 4.73)
print("Packed Data is " , packedData)


unpackedData = unpack('iif', packedData)
print("Unpacked Data is ",unpackedData)