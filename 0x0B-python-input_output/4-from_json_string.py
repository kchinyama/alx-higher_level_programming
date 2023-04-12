#!/usr/bin/python3
'''function returns an object (Python data structure) 
represented by a JSON string
'''

import json


def from_json_string(my_str):
    '''python data structure represnted in JSON
    '''
    return json.loads(my_str)
