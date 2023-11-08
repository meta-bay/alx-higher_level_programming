#!/usr/bin/python3
def complex_delete(dic, val):
    dels = [x for x in dic if dic[x] == val]
    for d in dels:
        del dic[d]
    return dic
