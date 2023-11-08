#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    copy_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j)
        copy_matrix.append(row)
    for i in range(len(copy_matrix)):
        for j in range(len(copy_matrix[i])):
            copy_matrix[i][j] = copy_matrix[i][j] ** 2
    return copy_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)