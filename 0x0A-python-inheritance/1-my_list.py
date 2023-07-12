#!/usr/bin/python3
"""
Module that print the List
"""


class MyList(list):
    """
    A class that that print list
    """
    def print_sorted(self):
        """
        A function that print list by asending
        """
        new = []
        sort = sorted(self)

        for i in sort:
            new.append(i)
        print(new)
