#!/usr/bin/python3
"""module that has the square class -also child of base
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        self .__size = size
        self.__x = x
        self.__y = y

        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """overided str method for square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter for size"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size

