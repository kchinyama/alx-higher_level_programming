#!/usr/bin/python3
"""module that demo' print list with class
"""

class MyList(list):
    """method that prints asceded list"""


    def print_sorted(self):
        """method that prints asceded list"""
        print(sorted(self))
