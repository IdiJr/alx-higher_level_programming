#!/usr/bin/python3
"""Defines a class rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The heigth of the new rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints the rectagle description and area"""
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string
