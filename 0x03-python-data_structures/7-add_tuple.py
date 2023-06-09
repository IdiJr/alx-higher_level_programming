#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    """Add two tuples and returns a tuple with 2 integers."""
    if len(tuple_a) == 0:
        tuple_a = 0, 0
    elif len(tuple_a) == 1:
        tuple_a = tuple_a[0], 0
    else:
        tuple_a = tuple_a[0], tuple_a[1]

    if len(tuple_b) == 0:
        tuple_b = 0, 0
    elif len(tuple_b) == 1:
        tuple_b = tuple_b[0], 0
    else:
        tuple_b = tuple_b[0], tuple_b[1]

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
