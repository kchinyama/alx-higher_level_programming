#!/usr/bin/python3
"""module that has the square class -also child of base
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """square constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        self .__size = size
        self.__x = x
        self.__y = y

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """overided str method for square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
    
    def update(self, *args, **kwargs):
        """args and kwargs method"""
        attris = ["id", "size", "x", "y"]

        if args:
            for arg, attri in zip(args, attris):
                setattr(self, attri, arg)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}


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

