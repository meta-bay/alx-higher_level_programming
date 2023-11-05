#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == len(matrix[i]) - 1:
                    print("{}".format(matrix[i][j]), end="$\n")
                else:
                    print("{}".format(matrix[i][j]), end=" ")
    else:
        print("$")