#!/usr/bin/python3
'''
    Pascal's Triangle
'''


def pascal_triangle(n):
    '''
        returns a list of lists of integers
        representing the Pascal's triangle of n
    '''
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([i+j for i, j
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
