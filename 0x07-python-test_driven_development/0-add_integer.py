#!/usr/bin/python3
'''
    add_integer module
'''


def add_integer(a, b=98):
    '''
        adds two integers
        raises typeError if they are not int or float
        returns their sum
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
