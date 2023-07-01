#!/usr/bin/python3
"""  Object to a text file using
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
