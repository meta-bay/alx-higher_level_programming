#!/usr/bin/python3
'''
    writes an Object to a text file, using a JSON representation
'''


import json


def save_to_json_file(obj, fname):
    '''
        write obj to f name
    '''
    with open(fname, "w") as f:
        f.write(json.dumps(obj))
