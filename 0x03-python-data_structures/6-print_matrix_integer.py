#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for k in range(len(matrix[row])):
                if k != len(matrix[row]) - 1:
                    end=' '
                else:
                    end=''
                print("{:d}".format(matrix[row][k]), end='')
            print()
