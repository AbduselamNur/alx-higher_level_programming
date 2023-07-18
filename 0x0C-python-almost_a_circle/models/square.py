#!/usr/bin/python3
"""Module of models/square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Intialization of Square Class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        string = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )
        return string
