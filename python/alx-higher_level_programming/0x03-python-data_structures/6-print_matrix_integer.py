#!/usr/bin/python3
"""function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    for row in matrix:
        print(matrix[row])
        if matrix is not None:
            print(end="")
            # print("{} ".format(matrix[row]))
        else:
            print()
