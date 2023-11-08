#!/usr/bin/python3

def best_score(a_dictionary):
    max_val = None
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        if max_val is None or value > max_val:
            max_val = value
            best_key = key
    return best_key
