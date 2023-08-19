#!/usr/bin/python3
def no_c(my_string):
    for k in my_string:
        new_string = my_string.translate({ord(k): None for k in 'cC'})
        return new_string
