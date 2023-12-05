#!/usr/bin/python3
'''
    Load, add, save
'''
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def arg_to_list():
    '''
         adds all arguments to a Python list
    '''
    f = "add_item.json"
    the_obj = []
    if os.path.exists(f):
        the_obj = load_from_json_file(f)
    the_args = the_obj + sys.argv[1:]
    save_to_json_file(the_args, f)


arg_to_list()
