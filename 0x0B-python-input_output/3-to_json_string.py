#!/usr/bin/python3
"""Module that convert object to json"""
import json


def to_json_string(my_obj):
    """
    a function that returns the JSON
    representation of an object (string)
    Args:
        my_obj (obj): object that convert to Json
    """
    j = json.dumps(my_obj)

    return j
