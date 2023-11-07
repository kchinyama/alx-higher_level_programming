#!/usr/bin/python3
"""module demo of that writes object to file using json
"""
import json


def save_to_json_file(my_obj, filename):
    """returns obj txt file in json format"""
    with open(filename, "w", encoding="utf-8") as k:
        json_format = json.dumps(my_obj)
        return (k.write(json_format))
        
