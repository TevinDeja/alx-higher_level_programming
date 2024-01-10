#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal’s triangle of n.
    """
    matrix = []
    for x in range(n):
        rows = []
        for y in range(x + 1):
            if y == 0 or y == x:
                result = 1
            else:
                result = matrix[x-1][y-1] + matrix[x-1][y]
            rows.append(result)
        matrix.append(rows)
    return matrix
