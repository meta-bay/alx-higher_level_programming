#!/usr/bin/python3
'''
    appending text
'''


def append_write(filename="", text=""):
    """
        appens to a file or create if it doesn't exists
    """
    with open(filename, "a", encoding='utf-8') as f:
        the_file = f.write(text)
    return the_file
