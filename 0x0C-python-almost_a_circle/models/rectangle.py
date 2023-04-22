#!/usr/bin/python3
"""simple rectangle class
"""

from base import Base

class Rectangle(Base):
    """rectangle class which inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """width getter"""
            return self.__width

        @width.setter
        def width(self, value):
            """width setter"""
            self.validate_int("width", value)
            self.__width = value


        @property
        def height(self):
            """height getter"""
            return self.__height

        @height.setter
        def height(self, value):
            """height setter"""
            self.validate_int("height", value)
            self.__height = value

        @property
        def x(self):
            """x getter"""
            return self.__x
        
        @x.setter
        def x(self, value):
            """x setter"""
            self.validate_int("x", value)
            self.__x = value

        @property
        def y(self):
            """y getter"""
            return self.__width
        
        @y.setter
        def y(self, value):
            """y setter"""
            self.validate_int("y", value)
            self.__y = value

        """now we write the validation method that further cleans up our input values"""
        def validate_int(self, data, value):
            """this validates the input"""
            if type(data) is not int:
                raise TypeError("{:s} must be an integer".format(data))
            if (data == "width" or data == "height") and value <= 0:
                raise ValueError("{:s} must be > 0".format(data))
            if (data == "x" or data == "y") and value <= 0:
                raise ValueError("{:s} must be > 0".format(data))

