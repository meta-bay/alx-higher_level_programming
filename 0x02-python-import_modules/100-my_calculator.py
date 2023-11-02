#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ex = 1
    a = int(sys.argv[1])
    o = sys.argv[2]
    b = int(sys.argv[3])
    op = [["+", add], ["-", sub], ["*", mul], ["/", div]]
    for c in op:
        if c[0] == o:
            print(f"{a} {o} {b} = {int(c[1](a, b))}")
            ex = 0
    if ex:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
