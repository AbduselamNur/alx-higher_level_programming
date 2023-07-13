#!/usr/bin/python3
"""
Module that return True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Function that Check Obj in a_class
    Args:
        obj: object
        a_class: classes
    Return:
        True:  if the object is exactly an instance of the specified class
        False: Return Otherwise
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
