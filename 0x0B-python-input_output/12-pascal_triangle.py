#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """
    a function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    t_r = [1]
    t_l = [0]
    p_t = []

    if n <= 0:
        return p_t

    for i in range(n):
        p_t.append(t_r)
        t_r = [x+r for x, r in zip(t_r + t_l, t_l + t_r)]
    return p_t
