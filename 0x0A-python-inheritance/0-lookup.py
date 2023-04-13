#!/usr/bin/python3
'''def lookup(obj) module
'''
def lookup(obj):
    '''function that returns the list of available attributes 
    and methods of an object
    '''
    total = 0

    for k in obj:
        total += k

    return list(total)
