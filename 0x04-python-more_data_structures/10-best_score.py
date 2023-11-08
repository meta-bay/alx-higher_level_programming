#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_key = max(a_dictionary, key=lambda i: a_dictionary[i])
        return max_key
    else:
        return None
