'''
Created on 12-Jul-2016

@author: zeeshan
'''
import threading

class  MyMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            
            
x = MyMessenger(name = 'Sending out message')
y = MyMessenger(name = 'Receive message')
x.start()
y.start()