#!/usr/bin/python3
"""
    Module: class Rectangle from BaseGeomerty
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle
    """
    def __init__(self, width, height):
        """
            initialises Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
            Returns area of a rectangle
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
            retruns rectangle details
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
