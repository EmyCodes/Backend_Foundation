#!usr/bin/python3
"""
function that computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix.
    """
    new_matrix = matrix[:]
    for row in new_matrix:
        rows = []
        for column in row:
            rows.append(column*2)
        return rows

