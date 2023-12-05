#!/usr/bin/python3
'''
    Pascal's Triangle
'''


def generate_pascal_triangle(n):
    '''
        returns a list of lists of integers
        representing the Pascal's triangle of n
    '''
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        left, right = prev_row[:-1], prev_row[1:]
        new_row = [1] + [sum(pair) for pair in zip(left, right)] + [1]
        triangle.append(new_row)
    return triangle
