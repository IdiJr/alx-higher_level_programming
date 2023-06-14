#!/usr/bin/python3


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n.
    Return: a list integers representing the triangle
    """
    triangle = [[1]]
    while len(triangle) != n:
        new_triangle = triangle[-1]
        tmp = [1]
        for i in range(len(new_triangle) - 1):
            tmp.append(new_triangle[i] + new_triangle[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
