#!/usr/bin/python3
'''function that writes an Object to a text file, using a JSON representation
'''

import json

def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a text file, 
    using a JSON representation. The use of with statement
    mandatory
    '''
    with open(filename, mode="w") as my_file:
        my_file.write(json.dumps(my_obj))
