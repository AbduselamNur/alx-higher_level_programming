#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for v in range(len(matrix[r])):
            if (v < (len(matrix[r])) - 1):
                print("{:d}".format(matrix[r][v]), end=" ")
            else:
                print("{:d}".format(matrix[r][v]), end="")
        print()
