#!/usr/bin/python3
""" Module class Student
"""


class Student:
    """ Class student instances """

    def __init__(self, first_name, last_name, age):
        """method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_l = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_l[satr] = obj[satr]
            return d_l

        return obj

    def reload_from_json(self, json):
        """ attributes of the Student instance """
        for atr in json:
            self.__dict__[atr] = json[atr]
