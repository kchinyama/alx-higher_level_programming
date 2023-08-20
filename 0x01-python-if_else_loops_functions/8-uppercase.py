#!/usr/bin/python3
def uppercase(str):
    for k in str:
        if ord(k) > 96 and ord(k) < 123:
            k = chr(ord(k) - 32)
        print("{}".format(k), end="")
    print("")
