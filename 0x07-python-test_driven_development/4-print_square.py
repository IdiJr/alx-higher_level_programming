#!/usr/bin/python3


def print_square(size):
    """Return: size of square printed with character "#"
    Args:
        Arg1: Type int the size of the square
        Raises: TypeError and ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
