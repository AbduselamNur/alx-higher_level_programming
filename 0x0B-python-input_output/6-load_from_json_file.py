#!/usr/bin/python3
""" Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ an Object from a JSON file

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
