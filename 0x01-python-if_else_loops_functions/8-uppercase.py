#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= ord('Z'):
            top = c
        else:
            top = chr(ord(c) - 32)
        print("{:s}".format(top), end='')
    print('')
