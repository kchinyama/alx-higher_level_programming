#!/usr/bin/python3
"""module that shows py object rep of json data
"""
import json


def from_json_string(my_str):
    """converts json data to python object"""
    return (json.loads(my_str))
