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
        """writes json string rep of list_objs to a file"""
        file_name = cls.__name__ + ".json"

        json_list = []

        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs] #convert each to dictionary

            json_string = cls.to_json_string(json_list) #json string rep of the list

            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(json_string) #open and write to the file


    @staticmethod
    def from_json_string(json_string):
        """method returns the list of the json string rep of json_string"""

        if json_string is None or len(json_string) == 0:
            return []

        else:
            return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """method auto updates attributes to an instance"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)

        if cls.__name__ == "Square":
            dummy = cls(2)

        dummy.update(**dictionary) # update dummy attribute values with those from dict

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances from a file"""

        file_name = cls.__name__ + 'json'

        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                info = f.read() # read content in file

                list_dict = cls.from_json_string(info) # convert json string to list of dictionaries

                list_ins = [] # variable to hold list of instances

                for k in list_dict: # iterate through the dictioneries
                    list_ins.append(cls.create(**k)) #create instance using built in create method

                return list_ins # return the list of instances

        except FileNotFoundError: # if file is no existant
            return [] # empty list
