#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length < 2:
        print("{}: arguments.".format(length - 1))
    if length == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    if length >= 3:
        print("{}: arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))