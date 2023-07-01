#!/usr/bin/python3
"""a function that reads from a file """


def read_file(filename=""):
    """ reads from a file

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
