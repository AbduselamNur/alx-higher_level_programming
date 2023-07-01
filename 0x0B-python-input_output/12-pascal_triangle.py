#!/usr/bin/python3
"""
    pascal_triangle: pascal_triangle()
"""


def pascal_triangle(n):
    """
        returns lists of integers
        Returns: list of lists
    """
    t_r = [1]
    temp_l = [0]
    p = []

    if n <= 0:
        return p

    for i in range(n):
        p.append(t_row)
        t_r = [l+r for l, r in zip(t_r + temp_l, temp_l + t_r)]
    return p
