#!/usr/bin/python3
'''class_to_json module'''

def class_to_json(obj):
    '''dictionary description of JSON serialized object
    '''
    return obj.__dict__
