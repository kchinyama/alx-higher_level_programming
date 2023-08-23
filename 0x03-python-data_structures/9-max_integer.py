#!/usr/bin/python3
def max_integer(my_list=[]):
#    new_list = my_list.sort()
    list_Len = len(my_list)

    if list_Len == 0:
        return
    else:
        my_list.sort()
        return my_list[-1]

