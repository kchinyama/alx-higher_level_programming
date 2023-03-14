#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    new_list = list(my_list)
    for k in new_list:
        if k / 2 == 0:
            new_list[k] = True
        else:
            new_list[k] = False
    return new_list
