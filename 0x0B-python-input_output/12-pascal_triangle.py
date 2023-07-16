#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """
    a function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    tri = [[1]]
    for r in range(1, n + 1):
        r_l = [1]
        for i in range(1, r):
            r_l.append(tri[r - 1][i - 1] + tri[r - 1][i])
        r_l.append(1)
        tri.append(r_l)
    return tri
