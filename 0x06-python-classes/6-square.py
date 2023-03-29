#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").MyClass.__doc__)'''
class Square:
    '''python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size

    '''getter for retrieving and presenting the data with more user appeal'''
    @property
    def size(self):
        return self.__size

    '''set setter in order to clean out the output'''
    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("message")
        if value[0] < 0 and value[1] < 0:
            raise TypeError("message")

    '''python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'''
    def area(self):
        '''definitions will follow here'''
        return self.__size ** 2

    def my_print(self):
        if size == 0:
            print("--")
        else:
            print("#",self.__size ** 2)
