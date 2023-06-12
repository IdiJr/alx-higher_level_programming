#!/usr/bin/python3
"""Defines a rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reprensents a rectangle with BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The heigth of the new rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
