#!/usr/bin/python3
if __name__ == "__main__":
    """imports all functions from the file calculator_1.py and handles basic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '*' and sys.argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    answer = ops[sys.argv[2]](a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, answer))
