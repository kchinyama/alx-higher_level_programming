#!/usr/bin/python3
""" declaration of class rectangle
"""
class Rectangle:
    """initialise puplic class variable that counts the number of each  instantiation
    """
    number_of_instances = 0

    """initialise public variable to print symbol
    """
    print_symbol = "#"

    """initialize init method for ease of copying and pasting subsequent methods
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        """increment by one everytime an instance is created
        """
        Rectangle.number_of_instances += 1

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

        return "\n".join(str(self.print_symbol) * self.__width
            for _ in range(self.__height))


    def __repr__(self):
        return ("{:s} ({:d}, {:d})".format(type(self).__name__, self.__width, self.__height))

    def __del__(self):
        """Removes/deletes an instance
        """
        print("Bye rectangle...")

        """decrement by one everytime an instance is deleted
        """
        Rectangle.number_of_instances -= 1

    
    """Initialise static method as instructed that returns largest the biggest
    rectangle by area
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """we want the largest rectangle by area, raise typerror if
        not instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_2

    """Initialise class method that returns new Rectangle instance
    """
    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
