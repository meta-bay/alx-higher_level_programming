#!/usr/bin/python3
'''
    text indentation module
'''


def text_indentation(text):
    '''
        prints a text with 2 new lines after each of these
        characters: '.', '?' and ':'
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    the_line = ''
    for char in text:
        the_line += char
        if char in ('.', '?', ':'):
            print(the_line.strip())
            print()
            the_line = ''

    if the_line:
        print(the_line.strip())
