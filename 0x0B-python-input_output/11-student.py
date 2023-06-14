#!/usr/bin/python3
"""Defines the class student"""


class Student:
    """Represents the class of a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student
        Args:
            Arg first_name(str): The first name of the student
            Arg last_name(str): The last name of the student
            Arg age(int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets dictionary representation of student.
        if attrs is a list of stringsonly attribute names
        contained in this list must be retrieved.
        Args:
            attrs(list): the attributes to be represented
        """
        if (type(attrs) == list and all(type(element) == str
                                        for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the student.
        Args:
            json(dict): the pairs to replace attributes with.
        """
        for i, j in json.items():
            setattr(self, i, j)
