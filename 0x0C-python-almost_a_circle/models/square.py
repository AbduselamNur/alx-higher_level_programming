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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            attr = ["id", "size", "x", "y"]

            for i, args in enumerate(args):
                setattr(self, attr[i], args)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        the dictionary representation of a Square
        """
        dict = {}

        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y

        return dict
