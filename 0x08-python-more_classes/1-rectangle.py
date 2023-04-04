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
        return self.width

    """initialize the width method as instructed, we want to set it
    """
    @width.setter
    #    """Protect it from bad values
    #    """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.width <= 0:
            raise ValueError("width must be >= 0")

    """initialize height method as instructed-getter.
    """
    @property
    def height(self):
        """Returns the height
        """
        return self.height

    """initialize the height method as instructed, we want to set it
    """
    @height.setter
    #"""Protect value from bad input values
    #"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if self.height <= 0:
            raise ValueError("height must be >= 0")
