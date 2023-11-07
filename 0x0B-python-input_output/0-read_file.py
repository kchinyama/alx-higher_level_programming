#!/usr/bin/python3
"""module demo' reads and prints to stdout
"""


def read_file(filename=""):
    """body of function"""

    with open(filename, "r", encoding="utf-8") as k:
        print(k.read(), end="")
