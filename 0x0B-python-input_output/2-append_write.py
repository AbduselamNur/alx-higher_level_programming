#!/usr/bin/python3
"""a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ appends to a text file

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
