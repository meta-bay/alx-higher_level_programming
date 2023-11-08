#!/usr/bin/python3
def square_matrix_map(mtrx=[]):
    return list(map(lambda x: list(map(lambda y: y * y, x)), mtrx))
