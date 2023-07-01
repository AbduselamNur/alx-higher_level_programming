#!/usr/bin/python3
"""a function that writes to a text file
"""


def write_file(filename="", text=""):
    """ Function that writes to a text file


    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
