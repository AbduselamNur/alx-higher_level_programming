#!/usr/bin/python3
"""Read file Module"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: file that read
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        cont = myfile.read()
    print(cont, end="")
