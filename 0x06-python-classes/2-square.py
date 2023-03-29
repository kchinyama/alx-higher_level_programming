#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").MyClass.__doc__)'''
class Square:
    '''python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'''
    def __init__(self, size=0):
        '''size initialised to 0 as instructed'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
