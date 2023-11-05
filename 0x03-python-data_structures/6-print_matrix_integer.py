#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for i in range(len(row)):
                print(row[i], end="")
                if i < len(row) - 1:
                    print(" ", end="")
            print("$")
