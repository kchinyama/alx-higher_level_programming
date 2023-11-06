#!/usr/bin/python3
"""module that checks instance of sub-class
"""


def inherits_from(obj, a_class):
    """function that uses built it is instance to check oject
    is has inherited from other class"""
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
