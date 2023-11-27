#!/usr/bin/python3
'''
    The module
'''
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N\n")
    sys.exit(1)
N = sys.argv[1]
if not N.isdigit():
    print("N must be a number\n")
    sys.exit(1)
N = int(N)
if N < 4:
    print("N must be at least 4\n")
    sys.exit(1)


def queens(N, i, a_l, b_l, c_l):
    '''
        solves The N queens puzzle
    '''
    solutions = []
    if i < N:
        for j in range(N):
            if j not in a_l and i + j not in b_l and i - j not in c_l:
                solutions.extend(queens(N, i + 1, a_l + [j],
                                        b_l + [i + j], c_l + [i - j]))
    else:
        solutions.append(a_l)
    return solutions


result = queens(N, 0, [], [], [])
for solution in result:
    print([[row, col] for row, col in enumerate(solution)])
