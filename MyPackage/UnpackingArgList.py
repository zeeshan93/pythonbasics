'''
Created on 05-Jul-2016

@author: zeeshan
'''
def unpack_arg_list(name,action,verb):
    print(name,action,verb)
    
unpackList = ['zeeshan','is','awesome']
unpack_arg_list(*unpackList)