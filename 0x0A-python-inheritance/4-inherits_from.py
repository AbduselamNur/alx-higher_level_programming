#!/usr/bin/python3
"""
Module returns True if the object is an instance of a class that inherited

(directly or indirectly) from the specified class;

otherwise False
"""


def inherits_from(obj, a_class):
    """
    A function that check inherited (directly or indirectly)

    from the specified class
    Argument:
        obj: first argument
        a_class: seconde aregument
    Return:
        True: if the object is an instance of a class that inherited
              (directly or indirectly) from the specified class
        False: Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
