#!/usr/bin/python3
"""
    Module: inherits_from()
"""


def inherits_from(obj, a_class):
    """
        inherits_from returns  instance of a class
        that inherited from the specified class.
        Args:
            obj (object): object Name.
            a_class (class): class Nmae.
        Returns: True , False.
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
