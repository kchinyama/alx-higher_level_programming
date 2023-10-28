#!/usr/bin/python3
"""
this module demo' a function that adds 2 ints
"""

def add_integer(a, b=98):
    """body of the function-returns the sum"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
