#!/usr/bin/python3
def print_last_digit(number):
    for k in number:
        if k == int(chr(number)[-1]):
            print(k)
    #print(int(chr(number)[-1]))
