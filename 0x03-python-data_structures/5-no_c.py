#!/usr/bin/python3
def no_c(my_string):
    new_string_list = list(my_string)
    letter_count = 0
    for k in new_string_list:
        if k == 'c' or k == 'C':
            new_string_list[letter_count] = ""
        letter_count = letter_count + 1
    return "".join(new_string_list)
