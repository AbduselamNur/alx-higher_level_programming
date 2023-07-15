#!/usr/bin/python3
"""Module that convert json to object and viceverse"""
import json


def from_json_string(my_str):
    """
    a function that returns an object
    (Python data structure) represented by a JSON string
    Args:
        my_str (json): json convert to string
    """
    j_s = json.loads(my_str)

    return j_s
