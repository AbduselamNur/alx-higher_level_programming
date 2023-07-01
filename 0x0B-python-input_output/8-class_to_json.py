#!/usr/bin/python3
""" description with a simple
"""


def class_to_json(obj):
    """ Function  description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
