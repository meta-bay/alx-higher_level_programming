#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    '''
        multiplies 2 matrices
    '''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(sub_list, list) for sub_list in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(sub_list, list) for sub_list in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    row_length_a = len(m_a[0])
    row_length_b = len(m_b[0])
    for i in m_a:
        if len(i) != row_length_a:
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if len(i) != row_length_b:
            raise TypeError("each row of m_b must be of the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    if row_length_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            num = 0
            for k in range(len(m_a[0])):
                num += m_a[i][k] * m_b[k][j]
            row.append(num)
        result.append(row)
    return result
