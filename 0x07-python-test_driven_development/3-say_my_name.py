#!/usr/bin/python3
"""
This Module Print firstname and lastname
"""


def say_my_name(first_name, last_name=""):
    """
    Function that print first and last Name

    Args:
        first_name (str): user first name
        last_name (str): user last name default: ""

    Raise:
        TypeError: first_name must be a string
                   last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
