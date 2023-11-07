#!/usr/bin/python3
"""demo module of append to file and char count
"""


def append_write(filename="", text=""):
    """body of function"""

    with open(filename, "a", encoding="utf-8") as k:
        k.write(text)

    return len(text)
