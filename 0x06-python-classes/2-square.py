#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").MyClass.__doc__)'''
class Square:
    '''python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'''
    def __init__(self, size=0):
        '''size initialised to 0 as instructed'''
        self.__size = size
        try:
            size > 0
        except TypeError:
            print("size must be an integer")
        try:
            size < 0
        except ValueError:
            print("size must be >= 0")
