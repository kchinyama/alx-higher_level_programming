#!/usr/bin/python3
'''function creates an Object from a “JSON file"
'''
import json

def load_from_json_file(filename):
    '''we want an object from a json file
    '''
    with open(filename, 'w') as my_file:
        return json.load(filename)
