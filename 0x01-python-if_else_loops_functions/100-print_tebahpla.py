#!/usr/bin/python3
for n in range(ord('Z'), ord('A') - 1, -1):
    if n % 2 == 0:
        ch = n + 32
    else:
        ch = n
    print("{}".format(chr(ch)), end='')
