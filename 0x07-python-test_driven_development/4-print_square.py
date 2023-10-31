#!/usr/bin/python3
"""
this module is a demo of print square funt
"""

def print_square(size):
    """body of print sqr function"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for k in range(int(size)):
        print("#" * int(size))
