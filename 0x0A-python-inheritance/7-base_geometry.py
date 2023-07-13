#!/usr/bin/python3
"""
Module that BaseGeometry Class
"""


class BaseGeometry:
    """
    class that is BaseGeometry
    """
    def area(self):
        """
        Raise:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Intiger validator
        Args:
            name (str): person name
            value (int): age
        Raise:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
