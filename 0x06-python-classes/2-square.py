#!/usr/bin/python3
"""No Module for this task
"""


class Square:
    """
    a class Square that defines a square

    Args:
        size (int): integer that is the size of squar
    """

    def __init__(self, size=0):
        """
        initialization of class

        Args:
            size (int): size of square
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
