#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for k in my_list:
        copy = [k for k in my_list]
        if idx < 0:
            return my_list
        elif idx > len(my_list) - 1:
            return my_list
        else:
            copy[idx] = element
            return copy
            
