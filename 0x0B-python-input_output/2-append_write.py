#!/usr/bin/python3
"""Append to a file Module"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Args:
        filename: name of the file that append
        text: text that append
    """
    with open(filename, "a") as myfile:
        cont = myfile.write(text)
    return cont
