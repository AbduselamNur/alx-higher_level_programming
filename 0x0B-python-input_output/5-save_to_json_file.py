#!/usr/bin/python3
"""json Module that conver json-str & Viceverse"""
import json


def save_to_json_file(my_obj, filename):
    """
     a function that writes an Object to a text file,
     using a JSON representation
     Args:
        my_obj: object that save in to filename
        filename: json filename that save
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
