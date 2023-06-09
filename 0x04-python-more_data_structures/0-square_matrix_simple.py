#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return [[]]
    if len(matrix[0]) == 0:
        return [[]]
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        new_matrix.append(new_row)
    return new_matrix
