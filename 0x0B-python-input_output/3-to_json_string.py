#!/usr/bin/python3
"""
    JSON representation of an object (string)
"""


import json


def to_json_string(obj):
    """
        JSON dumper
    """
    return json.dumps(obj)
