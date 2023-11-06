#!/usr/bin/python3
"""module that tests instance is exactly of spec class
"""


def is_same_class(obj, a_class):
    """conditional check for exacttness of instance"""

    return type(obj) is a_class
