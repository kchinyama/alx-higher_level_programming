#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in matrix]))
