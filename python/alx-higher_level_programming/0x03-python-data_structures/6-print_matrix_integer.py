#!/usr/bin/python3
"""function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    for i in matrix:
        for j in i:
            print("{:d}".format(j, end=" ")
