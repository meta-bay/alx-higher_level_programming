#!/usr/bin/python3
'''
    Pascal's Triangle
'''


def generate_pascal_triangle(n):
    '''
        returns a list of lists of integers
        representing the Pascal's triangle of n
    '''
    triangle = []
    ptr = 1
    if n <= 0:
        return triangle
    triangle = [[1], [1, 1]]
    if n == 1:
        return triangle[:-1]
    for i in range(2, n):
        temp = triangle[ptr]
        ptr += 1

        temp_l = [1]
        for j in range(len(temp)):
            if j + 1 < len(temp):
                temp_l.append(temp[j] + temp[j + 1])
            else:
                temp_l.append(1)
                triangle.append(temp_l)
                break
    return triangle
