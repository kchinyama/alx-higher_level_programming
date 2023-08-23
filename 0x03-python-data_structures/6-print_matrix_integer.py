#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for k in range(len(matrix[row])):
            if k != 0:
                print(" ", end="")
            print("{:d}".format(matrix[row][k]), end="")
        print()
