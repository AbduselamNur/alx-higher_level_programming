#!/usr/bin/python3
"""
    class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square implements
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialises
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            returns square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            sets size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            Args:
                *args -   no-keyword args
                **kwargs - number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            str function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            Returns representation of a Square
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
