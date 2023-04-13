#!/usr/bin/python3
'''a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
'''

class Student:
    '''Instantiation with first_name, last_name and age
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    '''public instance that retrieves a dictionary
    '''
    def to_json(self, attrs=None):
        '''initialize a variable that will hold the existance of a list'''
        the_list = True

        '''create if statement that checks for the existance of a list'''
        if not isinstance(the_list, list):
            the_list = False

        else:
            for k in attrs:
                if not isinstance(k, str):
                    the_list = False

        if not the_list:
            return self.__dict__

        else:
            dxnary = {}
            for attr in attrs:
                if attr in self.__dict__:
                    dxnary[attr] = self.__dict__.get(attr)
            return dxnary
