#!/usr/bin/python3

"""
function prints the first and last names
"""

def say_my_name(first_name, last_name=""):
    """body of the function checking the output"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
