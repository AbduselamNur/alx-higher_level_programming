#!/usr/bin/python3
"""Write to a file Module"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename: file name that write
        text: text that want to write
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        cont = myfile.write(text)
    return cont
