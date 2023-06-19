#!/usr/bin/python3
"""Defines Module Base class"""
import json
import csv
import turtle


class Base:
    """base class
    private class attribute:
        __nb_objects (int): number of instatiated base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes class when started"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation"""
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to json file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns a dictionary"""
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with “dummy” mandatory attributes"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(width=5, height=4, y=1, x=2)
        else:
            new_instance = cls(size=5, y=1, x=2)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV
        Args:
            Arg list_objs (list): list of inherited base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None:
                f.write("")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV
        Returns:
            a list of instantiated classes
            else, an empty list
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dictionaries = csv.DictReader(csvfile,
                                                   fieldnames=fieldnames)
                list_dictionaries = [dict([i, int(j)]for i, j in dicti.items())
                                     for dicti in list_dictionaries]
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws a square and rectangle using the turtle graphics module"""
        turt = turtle.Turtle()
        turt.pensize(3)
        turt.shape("arrow")

        turt.color("blue")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for i in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("red")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for i in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
            turt.hideturtle()

        turtle.done()
