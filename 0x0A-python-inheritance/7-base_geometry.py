#!/usr/bin/python3

'''My empty class
'''

class BaseGeometry:
    '''raises Exception with the message'''
    def area(self):
        '''like this'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
