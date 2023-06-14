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

    def to_json(self):
        """Gets a dictionary representation of student"""
        return self.__dict__
