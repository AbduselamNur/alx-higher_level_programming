#!/usr/bin/python3
""" Module that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends in new line found

    Args:
        filename: file_name
        search_string: string thatsearch
        new_string: string to append in the str

    """

    r_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            r_line += [line]
            if line.find(search_string) != -1:
                r_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(r_line))
