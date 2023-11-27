#!/usr/bin/python3
'''
    lazy matrix multiplication with numpy
'''
import numpy


def lazy_matrix_mul(m_a, m_b):
    '''
        multiplying matrix using numpy
    '''
    try:
        result = numpy.matmul(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("Matrices cannot be multiplied") from e
    except TypeError as e:
        raise TypeError("The matrices must have valid input") from e
