#!/usr/bin/python3
'''
    file reading
'''


def read_file(filename=""):
    '''
        a funciton that reads a file
    '''
    with open(filename, encoding="utf-8") as f:
        for i in f:
            print(i)
