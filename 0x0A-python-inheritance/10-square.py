#!/usr/bin/python3
"""Defines a subclass square of Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Type class of a square inherit a rectangle"""

    def __init__(self, size):
        """Initializes a square instance
        Args:
            size (int): The size of the square
        Raises: ValueError if size is not a positive integer.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)

    def __str__(self):
        """Prints the rectangle's description and area"""
        return f"[Rectangle] {self.__size}/{self.__size}"
