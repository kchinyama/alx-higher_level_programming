#!/usr/bin/python3
'''this is a module for reading a file in python
'''
def read_file(filename=""):
    '''reading a file using the 'with' method
    '''
    with open("filename", 'r', encoding="utf-8") as my_file:
        print(my_file.read())
