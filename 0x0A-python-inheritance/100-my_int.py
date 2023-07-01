#!/usr/bin/python3
"""
    100-my_int: class MyInt
"""


class MyInt(int):
    """
        MyInt implements int. (inherits)
    """
    def __init__(self, number):
        self.number = number

    def __n__(self, value):
        return (self.number == value)

    def __e__(self, value):
        return (self.number != value)

    def __s__(self):
        return (str(self.number))
