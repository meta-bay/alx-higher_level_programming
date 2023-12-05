#!/usr/bin/python3
'''
    function to write
'''


def write_file(filename="", text=""):
    '''
        writes to a file
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        the_text = f.write(text)
    return the_text
