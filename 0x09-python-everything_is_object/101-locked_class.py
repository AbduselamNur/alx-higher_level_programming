#!/usr/bin/python3
class LockedClass:
    """
    class, that prevents the user from dynamically creating new instance attributes
    """

    __slots__ = ["first_name"]

    def __init__(self, first_name=None):
        """
        initiallize the class
        """
        if first_name is not None:
            self.first_name = first_name
