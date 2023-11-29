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
    indented_text = ''
    char_coll = ''
    for char in text.strip():
        if char in ['?', ':', '.']:
            char_coll += char
            char_coll = char_coll.strip()
            indented_text += char_coll + '\n\n'
            char_coll = ''
        else:
            char_coll += char
    indented_text += char_coll.strip()
    print(indented_text, end='')
