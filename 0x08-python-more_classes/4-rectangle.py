#!/usr/bin/python3
"""

There is No Module for this Task


"""


class Rectangle:
    """ Rectangle class that defined """

    def __init__(self, width=0, height=0):
        """  initializes the instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle


        """
        self.width = width
        self.height = height

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

    def area(self):
        """
        function that multiply the width and height

        Return:
            return width * height
        """

        return self.width * self.height

    def perimeter(self):
        """
        funtion of perimeter that return perimeter

        Return:
            return (2*width) + (2*height)
        """
        perm = (2 * self.width) + (2 * self.height)

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return perm

    def __str__(self):
        """
        special function that conver object in to str
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for i in range(self.height):
                string += ("#" * self.width) + "\n"
            return string[:-1]
    def __repr__(self):
        """
        represent the rectangle class
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
