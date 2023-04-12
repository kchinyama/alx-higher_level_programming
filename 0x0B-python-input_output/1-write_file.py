#!/usr/bin/python3
'''function writes a string and returns the number
of characters
'''

def write_file(filename="", text=""):
    '''write file on a file, function overwrites
    previous contents if file already exists
    '''
    with open("filename", mode='w', encoding="utf-8") as my_file:
        return my_file.write(text)
