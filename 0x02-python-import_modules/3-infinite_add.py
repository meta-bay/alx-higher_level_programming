#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print(0)
    if length > 1:
        sum = 0
        for i in range(1, length):
            value = int(sys.argv[i])
            sum += value
        print(sum)