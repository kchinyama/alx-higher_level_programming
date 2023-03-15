#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    square = lambda k: k**2
    for k in matrix:
        new_matrix.append(square(k))
    return new_matrix
