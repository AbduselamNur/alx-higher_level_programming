#!/usr/bin/python3
"""
Module that returns True if the object is an instance of, or if the object

is an instance of a class that inherited from, the specified class;

otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Function that check instance of class
    and inherted from

    Args:
        obj: first argument
        a_class: sec argument
    Return:
        True: if the object is an instance of, or if the
              object is an instance of a class that inherited from
        False: Otherwise
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    else:
        return False
