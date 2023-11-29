#!/usr/bin/python3
'''
    lazy matrix multiplication with numpy
'''
import numpy


def lazy_matrix_mul(m_a, m_b):
    '''
        multiplying matrix using numpy
    '''
    result = numpy.matmul(m_a, m_b)
    return result
