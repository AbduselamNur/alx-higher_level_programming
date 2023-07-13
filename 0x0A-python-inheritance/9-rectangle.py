#!/usr/bin/python3
"""
Module of Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        constractor
        Args:
            width (int): private integer
            heigth (int): private integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area that multiply width and Height"""
        return self.__width * self.__height

    def __str__(self):
        """Return String Format"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
