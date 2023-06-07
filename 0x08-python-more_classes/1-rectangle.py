#!/usr/bin/python3
"""

There is No Module in this Task

"""


class Rectangle:
    """
    Define Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        init function is initialize the reactangle class

        Args:
            width (int): width of the Reactangle
            height (int): height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width function is retrive the private instance

        Return:
            return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width function that set the private instance

        Args:
            value (int): the value of the width
        Raise:
            TypeError: width must be an integer
            ValueError width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height function that retrive the height private

        Return:
            return self private height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        heigth function that set height private instance

        Args:
            value: the height value
        Raise:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
