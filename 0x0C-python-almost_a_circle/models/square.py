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
