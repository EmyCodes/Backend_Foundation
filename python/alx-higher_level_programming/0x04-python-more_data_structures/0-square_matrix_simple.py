#!usr/bin/python3
"""
function that computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix.
    """
    new_matrix = matrix[:]
    new_matrix_ = []
    for row in new_matrix:
        rows = []
        for column in row:
            rows.append(column ** 2)
        new_matrix_.append(rows)
    return new_matrix_
