#!/usr/bin/python3
"""
This module is divied matrix ny div
"""


def matrix_divided(matrix, div):
    """
    function that divied matrix list by div
    and return new matrix

    Args:
        matrix (int): list of matrix
        div (int): division execpt 0
    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    Return:
        return new matrix
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err)
    for r in matrix:
        if not isinstance(r, (list, int, float)):
            raise TypeError(err)
        elif not isinstance(r, list):
            raise TypeError(err)
        elif len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for r in matrix:
        new_row = []
        for e in r:
            new = round(e/div, 2)
            new_row.append(new)
        new_matrix.append(new_row)
    return new_matrix
