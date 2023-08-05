#!/usr/bin/python3
"""function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    for i in range(0, len(matrix)):
        #print(matrix[i])
        for j in range(0, len(matrix[i])):
            print("{:d} ".format(matrix[i][j]))
