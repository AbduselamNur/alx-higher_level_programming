#!/usr/bin/python3
"""models/base.py"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
         that returns the JSON string
         representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        l_d = []
        if list_objs is not None:
            for i in list_objs:
                l_d.append(i.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(l_d))
