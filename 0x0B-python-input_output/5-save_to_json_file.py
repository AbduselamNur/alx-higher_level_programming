#!/usr/bin/python3
"""json Module that conver json-str & Viceverse"""
import json
from_json_string = __import__('4-from_json_string').from_json_string
to_json_string = __import__('3-to_json_string').to_json_string


def save_to_json_file(my_obj, filename):
    """
     a function that writes an Object to a text file,
     using a JSON representation
     Args:
        my_obj: object that save in to filename
        filename: json filename that save
    """
    new = to_json_string(my_obj)
    with open(filename, "w") as f:
        cont = f.write(new)
    return cont
