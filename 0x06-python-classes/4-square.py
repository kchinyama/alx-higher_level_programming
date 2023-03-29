#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").MyClass.__doc__)'''
class Square:
    '''python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'''
    def __init__(self, size=0):
        self.size = size

    '''python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'''
    def area(self):
        '''definitions will follow here'''
        return self.__size ** 2

    '''getter for retrieving and presenting the data with more user appeal'''
    @property
    def size(self):
        return self.__size

    '''set setter in order to clean out the output'''
    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
