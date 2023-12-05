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

    p_triangle = [[1]]

    for i in range(1, n):
        prev_row = p_triangle[-1]
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        p_triangle.append(new_row)

    return p_triangle
