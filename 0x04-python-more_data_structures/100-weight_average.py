#!/usr/bin/python3
def weight_average(ls=[]):
    if ls is None or ls == []:
        return 0
    scr = 0
    tms = 0
    for x in ls:
        scr += x[0] * x[1]
        tms += x[1]
    return scr / tms
