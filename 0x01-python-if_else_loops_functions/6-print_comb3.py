#!/usr/bin/python3
for fnum in range(10):
    for snum in range(fnum + 1, 10):
        if fnum < 8:
            print("{}{}".format(fnum, snum), end=', ')

    if fnum + 1 == snum:
        print(f"{fnum}{snum}")
