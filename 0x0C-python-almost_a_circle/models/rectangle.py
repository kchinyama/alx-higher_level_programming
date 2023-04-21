#!/usr/bin/python3
"""simple rectangle class
"""

from base import Base

class Rectangle(Base):
    """rectangle class which inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

        super().__init__(id=None)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if value .isdigit():
                self.__width = value
            else:
                raise TypeError("width must be a positive number")

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if value .isdigit():
                self.__height = value
            else:
                raise TypeError("height must be a positive number")

        @property
        def x(self):
            return self.__x
        
        @width.setter
        def x(self, value):
            if value .isdigit():
                self.__x = value
            else:
                raise TypeError("x must be a positive number")

        @property
        def width(self):
            return self.__width
        
        @width.setter
        def y(self, value):
            if value .isdigit():
                self.__y = value
            else:
                raise TypeError("y must be a positive number")
