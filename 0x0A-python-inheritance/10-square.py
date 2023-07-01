#!/usr/bin/python3
"""
    Module: class Square from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Attributes:
            size (int): side of square
    """
    def __init__(self, size):
        """
            initialises
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
            Returns square
        """
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[{}] {}/{}".format("Rectangle",
                                    self.__size, self.__size))
