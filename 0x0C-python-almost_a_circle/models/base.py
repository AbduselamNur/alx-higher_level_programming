#!/usr/bin/python3
import json
"""models/base.py"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Intialization of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
         that returns the JSON string
         representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)
