#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").MyClass.__doc__)'''
class Square:
    '''python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'''
    def __init__(self, size=None):
        '''size initialised to None but will be updated subsequently'''
        self.__size = size
