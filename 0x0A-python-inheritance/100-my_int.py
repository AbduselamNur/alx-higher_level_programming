#!/usr/bin/python3
"""
MyInt class module.


"""


class MyInt(int):
    """Define MyInt."""

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
