#!/usr/bin/python3
"""
    Module : is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class  instance of class.
        Args:
            obj (object): object nme.
            a_class (class): class name.
        Return: True , false.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
