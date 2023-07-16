#!/usr/bin/python3
"""JSON serialization of an object"""


def class_to_json(obj):
    """
     a function that returns the dictionary description with
     simple data structure (list, dictionary, string,
     integer and boolean) for JSON serialization of an object
     Args:
        obj:  is an instance of a Class
    """
    j_d = {}

    if hasattr(obj, "__dict__"):
        j_d = obj.__dict__.copy()
    return j_d
