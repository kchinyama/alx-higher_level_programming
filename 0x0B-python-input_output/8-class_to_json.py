#!/usr/bin/python3
"""module demo dictionary description with simple data structure
for json serialization of obj
"""


def class_to_json(obj):
    return obj.__dict__
