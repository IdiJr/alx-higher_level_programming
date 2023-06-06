#!/usr/bin/python3
"""A Class that defines a rectangle"""


class Rectangle:
    """Repressents a rectangle.
    Attributes:
        number_of_instances (int): the number of rectangle instances.
        print_symbol (any): the symbol used for the string representation
        of the rectangle.
        """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise a new rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
            """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with biggest area.
        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
            Raises:
                TypeError: If either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @property
    def height(self):
        """gets/sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
    """gets/sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns the printable reprisentation of the rectangle
        prints the rectagle with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))
             for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle = rectangle + ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Prints a message for every deletion of a rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
