#!/usr/bin/python3
"""module that demo' JSON rep of str
"""
import json


def to_json_string(my_obj):
    """convert obj to json format"""
    return (json.dumps(my_obj))
