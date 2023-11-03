#!/usr/bin/python3
"""function divides elements in a matrix
"""

def matrix_divided(matrix, div):
    """function body"""
    result = []
    length = 0

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        result.append(new_row)

    return result
