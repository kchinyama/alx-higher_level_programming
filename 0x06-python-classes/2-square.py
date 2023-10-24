#!/usr/bin/python3

"""
this is a square class
"""
class Square:
    """body of class to follow"""
    def __init__(self, size=0):
        """initialise the square"""

        '''if conditional'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
