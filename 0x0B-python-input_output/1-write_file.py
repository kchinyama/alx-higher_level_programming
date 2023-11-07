#!/usr/bin/python3
"""module that demo' str count to stdout
"""


def write_file(filename="", text=""):
    """body of function"""

    with open(filename, "w", encoding="utf-8") as k:
        k.write(text)

    return len(text)
