#!/usr/bin/python3
""" declaration of class rectangle
"""
class Rectangle:
    """initialize init method for ease of copying and pasting subsequent methods
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """initialize width method as instructed-getter.
    """
    @property
    def width(self):
        """Returns the width
        """
        return self.__width

    """initialize the width method as instructed, we want to set it
    """
    @width.setter
    #    """Protect it from bad values
    #    """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """initialize height method as instructed-getter.
    """
    @property
    def height(self):
        """Returns the height
        """
        return self.__height

    """initialize the height method as instructed, we want to set it
    """
    @height.setter
    #"""Protect value from bad input values
    #"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        """initialize public method area as instructed
        """
    def area(self):
        """ area is height x width. Returns computed number
        """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter is the distance around the circumfrance of the shape
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        """ computed perimeter when width and length values are not zero
        """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns instructed print format
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        size = "#" * self.__width
        string = ""

        for k in range(self.__height):
            if k == self.__height - 1:
                string += size

            else:
                string += (size + "\n")
        return string

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
