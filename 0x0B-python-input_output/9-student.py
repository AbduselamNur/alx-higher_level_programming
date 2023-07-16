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

    def to_json(self):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        j_d = {}

        if hasattr(self, "__dict__"):
            j_d = self.__dict__.copy()
        return j_d
