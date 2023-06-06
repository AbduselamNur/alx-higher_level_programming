#!/usr/bin/python3
"""
There is No Module in this task
"""


class Rectangle:
    """
    define Reactangle class name
    """
    __width = None

    @property
    def width(self):
        """
        funtion that retrive width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        funtion that set the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    __height = None

    @property
    def height(self):
        """
        Funtion that retrive
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Function that set the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be")
        elif value < 0:
            raise ValueError("height must be")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """
        Function That Initialize the class
        """
        self.height = height
        self.width = width
