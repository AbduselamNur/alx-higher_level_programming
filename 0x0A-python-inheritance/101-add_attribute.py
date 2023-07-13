#!/usr/bin/python3
"""attribute module"""


def add_attribute(obj, name, value):
    """Add a new attribute

    Args:
        obj (object): The object
        name (str): The name of attribute
        value (any): The value of attribute

    Raises:
        TypeError: If the object can't have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
