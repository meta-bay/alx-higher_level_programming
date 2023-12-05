#!/usr/bin/python3
'''
    Search and update
'''


def append_after(filename="", search_string="", new_string=""):
    '''
        inserts a line of text to a file
    '''
    the_lines = []
    with open(filename, "r", encoding="utf-8") as f:
        the_lines = f.readlines()
        i = 0
        while i < len(the_lines):
            if search_string in the_lines[i]:
                the_lines[i:i + 1] = [the_lines[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(the_lines)
