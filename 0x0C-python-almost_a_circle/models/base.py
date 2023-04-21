#!/usr/bin/python3
"""simple module that will be the base for all other classes in this project
"""

class Base:
    """parent class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

