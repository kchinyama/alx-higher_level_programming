#!/usr/bin/python3
def max_integer(my_list=[]):
    maxInt = my_list[0]
    for num in my_list:
        if my_list < 0:
            return None
        if num > maxInt:
            maxInt = num
            return maxInt
