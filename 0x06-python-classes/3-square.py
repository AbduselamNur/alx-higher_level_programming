#!/usr/bin/python3
"""No Module in this task
"""


class Square:
    """
    Square class is declared
    """
    __size = None

    def __init__(self, size=0):
        """
        Initialize square class

        Args:
            size (int) : size of square
        Raise:
            TypeError: when size not integer
            ValueError: When size less than zerro
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Area = size * size: this funtion return
        the area of square by Multiply of size
        """
        sq = self.__size * self.__size
        return sq
