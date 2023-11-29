#!/usr/bin/python3
'''
    matrix division module
'''


def matrix_divided(matrix, div):
    '''
    a function that divides all elements of a matrix
    Args:
        matrix: the matrix
        div: the divisor
    Return: a new matrix
    '''
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for i in matrix:
        if not isinstance(i, list) or not i:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        column = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
                                 of integers/floats")
            new_value = round(j / div, 2)
            column.append(new_value)
        result.append(column)
    return result
