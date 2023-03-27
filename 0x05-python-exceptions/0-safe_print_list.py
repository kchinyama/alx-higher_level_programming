#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end="")
            total = total + 1
        except IndexError:
            print()
            return total
