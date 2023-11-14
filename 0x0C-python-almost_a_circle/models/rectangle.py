#!usr/bin/python3
"""the rectangle class - child of Base
"""


from models.base import Base


class Rectangle(Base):
    """constructor method for rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    def area(self):
        """public method that returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """method display rectangle as #"""
        space = ' ' * self.x

        print('\n' * self.y, end='')

        for k in range(self.height):
            print(space + "#" * self.width)

    def __str__(self):
        """str method overide to print custom message"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update method that assigns arguments to each attribute"""
        attris = ["id", "width", "height", "x", "y"]

        if args:
            for arg, attri in zip(args, attris):
                setattr(self, attri, arg)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dictionary(self):
        """method that returns dict version of object"""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
