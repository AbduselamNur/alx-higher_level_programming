#!/usr/bin/python3
""" a function that returns the JSON
"""
import json


def to_json_string(my_obj):
    """ JSON representation of an object


    Raises:
        Exception: when the object can't be encoded

    """
    return json.dumps(my_obj)
