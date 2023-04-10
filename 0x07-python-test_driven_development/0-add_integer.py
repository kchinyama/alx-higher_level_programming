#!/usr/bin/python3

'''
function adds 2 intergers, both must be float or int
'''

def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
