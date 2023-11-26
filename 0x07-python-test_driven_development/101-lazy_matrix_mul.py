#!/usr/bin/python3
'''
    lazy matrix multiplication with numpy
'''
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    '''
        multiplying matrix using numpy
    '''
    return matmul(m_a, m_b)
