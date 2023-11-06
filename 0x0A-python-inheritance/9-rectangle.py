#!/usr/bin/python3
"""demo of class in alx
"""


class BaseGeometry:
    """public method area"""
    def area(self):

#        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.__name = name
        self.__value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


"""initialisation of new class Rectangle
"""


class Rectangle(BaseGeometry):
    """init constructor"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
