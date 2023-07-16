#!/usr/bin/python3
"""
Student to JSON Module"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Inntialization of Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return vars(self)
        else:
            n = {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
                }
            return n

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for i in json:
            self.__dict__[i] = json[i]
