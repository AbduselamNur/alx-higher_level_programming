#!/usr/bin/python3
"""
Module that print in two new line
"""


def text_indentation(text):
    """
     a function that prints a text with 2 new lines
     after each of these characters: ., ? and

    Args:
        text (str): string that print
    Raise:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    full = text[:]

    for i in ".?:":
        cha = full.split(i)
        full = ""
        for j in cha:
            j = j.strip(" ")
            full = j + i if full == "" else full + "\n\n" + j + i
    print(full[:-3], end="")
