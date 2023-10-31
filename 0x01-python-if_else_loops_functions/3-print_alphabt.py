#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if (chr(c) != 'q' and chr(c) != 'e'):
        print("{0}".format(chr(c)), end='')
