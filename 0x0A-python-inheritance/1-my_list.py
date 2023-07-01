#!/usr/bin/python3
"""
    class MyList
"""


class MyList(list):
    """
        class inherits from list.
        Attributes:
        Methods:
            print_sorted - prints the listr
    """
    def print_sorted(self):
        """
           prints a list.
        """
        print(sorted(self))
