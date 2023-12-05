#!/usr/bin/python3
'''
    file reading
'''


def read_file(filename=""):
    '''
        a funciton that reads a file
    '''
    with open(filename, mode="r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
