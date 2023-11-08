#!/usr/bin/python3
def roman_to_int(rm):
    if not isinstance(rm, str) or rm is None:
        return 0
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    leng = len(rm)
    for n in range(leng):
        if n > 0 and rome[rm[n]] > rome[rm[n - 1]]:
            num += (rome[rm[n]] - (rome[rm[n - 1]] * 2))
        else:
            num += rome[rm[n]]
    return num
