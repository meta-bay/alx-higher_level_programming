#!/usr/bin/python3
'''
    (Python data structure) represented by a JSON string
'''
import json


def from_json_string(str):
    '''
        From JSON string to Objec
    '''
    return json.loads(str)
