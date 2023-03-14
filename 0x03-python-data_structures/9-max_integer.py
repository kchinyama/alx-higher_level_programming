#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest_int = 0
    for k in my_list:
        if k > biggest_int:
            biggest_int = k
    return biggest_int
