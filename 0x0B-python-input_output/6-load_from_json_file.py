#!/usr/bin/python3
"""module demo' the creation of py obj from json file
"""
import json


def load_from_json_file(filename):
    """function converts from json to obj"""
    with open(filename, "r", encoding="utf-8") as k:
        content = k.read()
        obj = json.loads(content)
        return obj
