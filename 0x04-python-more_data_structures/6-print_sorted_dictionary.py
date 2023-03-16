#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_keys = list(a_dictionary)
    ordered_keys.sort()
    sorted_keys = {k: a_dictionary[k] for k in ordered_keys}
    return sorted_keys
