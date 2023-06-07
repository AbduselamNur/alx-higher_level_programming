#!/usr/bin/python3
"""

There is No Module for this Task


"""


class Rectangle:
    """ Rectangle class that defined """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """  initializes the instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle


        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ function method that returns the value of the width

        Returns:
            return the the self privat width of the rectangle


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ function method that defines the width

        Args:
            value: width of the reactangle

        Raises:
            TypeError: if width is not an integer rasie  TypeError
            ValueError: if width is less than zero raise ValueError


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Function method that returns the value of the height

        Returns:
            return the self height of the rectangle


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer raise TypeError
            ValueError: if height is less than zero raise ValueError


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
