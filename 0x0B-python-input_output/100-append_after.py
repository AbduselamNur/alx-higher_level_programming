#!/usr/bin/python3
"""executes a function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line string found

    Args:
        filename: filename that read
        search_string: string
        new_string: string that append

    """

    r_l = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            r_l += [line]
            if line.find(search_string) != -1:
                r_l += [new_string]

    with open(filename, 'w', encoding="utf-8") as fi:
        fi.write("".join(r_l))
