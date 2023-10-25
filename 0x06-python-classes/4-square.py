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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if self.__checkSize(value):
            self.__size = value


    def area(self):
        """public instance method for area calculation"""
        return int(self.__size) * int(self.__size)

    def __checkSize(self, size):
        """checks for error inputs in size"""
        if type(size) != int:
            raise TypeError("size must be an interger")

        elif size < 0:
            raise ValueError("size must be greater than 0")

        else:
            return True
        return False
