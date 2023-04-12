#!/usr/bin/python3
'''function appends data onto a file
'''
def append_write(filename="", text=""):
    '''the use of with is mandatory'''
    with open("filename", "a", encoding="utf-8") as my_file:
        my_file.write(text)
