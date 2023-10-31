#!/usr/bin/python3
"""
demo module that prints custom text
"""

def text_indentation(text):
    """conditional for desired output"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    replace = {'.': '.\n\n', '?': '?\n\n', ':': ':\n\n'}
    for old, new in replace.items():
        text = text.replace(old, new)
    print("\n".join([line.strip() for line in text.split("\n")]), end="")
