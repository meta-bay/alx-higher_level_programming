#!/usr/bin/python3
'''
    Object from a “JSON file”
'''


import json


def load_from_json_file(filename):
    '''
        create object from json
    '''
    with open(filename, "r") as f:
        obj = json.loads(f.read())
    return obj
