#!/usr/bin/python3
def no_c(my_string):
    for k in my_string:
        new_string = my_string.translate({ord(k): None for k in 'cC'})
        if k == 'c' and k == 'C':
            return my_string
        else:
            return new_string
