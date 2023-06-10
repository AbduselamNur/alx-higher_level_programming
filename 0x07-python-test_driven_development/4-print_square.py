#!/usr/bin/python3
""" This module print square
"""


def print_square(size):
    """
    function that print square
    by # symbole

    Args:
        size (int): size of the square

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
