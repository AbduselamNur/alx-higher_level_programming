#!/usr/bin/python3
"""Module models/rectangle.py"""
from models.base import Base


class Rectangle(Base):
    """
    the class Rectangle that inherits from Base
    """

    __width = None
    __height = None
    __x = None
    __y = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Intialize the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """area that multiply width by height"""
        return self.width * self.height

    def display(self):
        """
         prints in stdout the Rectangle
         instance with the character #
         """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )
        return string

    def update(self, *args, **kwargs):
        """set with index"""
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle"""
        dict = {}

        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y

        return dict
