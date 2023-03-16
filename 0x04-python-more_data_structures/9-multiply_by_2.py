#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp = dict(a_dictionary)
    for k, value in temp.items():
        temp[k] = value*2
    return temp
