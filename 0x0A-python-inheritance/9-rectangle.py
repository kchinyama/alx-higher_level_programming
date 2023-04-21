#!/usr/bin/python3

'''import parent class
'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    '''rectangle class that inherits from parent-BaseGeometry
    '''
    def __init__(self, width, height):
        '''private instance arguments'''
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    '''invoke the area function in parent class
    super()
