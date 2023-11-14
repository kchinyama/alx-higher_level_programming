#!/usr/bin/python3
"""module that demo's the base parent class
"""


import json

class Base:
    """the base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns json representation of data"""

        if list_dictionaries == None:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes json str rep of class objects"""

        for k in list_objs:
            with open(k, 'w', encoding='utf-8') as new_file:
                json.dumps(new_file)
