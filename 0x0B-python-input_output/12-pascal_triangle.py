#!/usr/bin/python3
"""
    12-pascal_triangle: pascal_triangle()
"""


def pascal_triangle(n):
    """
        Returns: list of lists
    """
    t_row = [1]
    temp_l = [0]
    p = []

    if n <= 0:
        return p

    for i in range(n):
        p.append(t_row)
        t_row = [l+r for l, r in zip(t_row + temp_l, temp_l + t_row)]
    return p
