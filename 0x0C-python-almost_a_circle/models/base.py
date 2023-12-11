#!/usr/bin/python3
'''
    Base class module
'''
import json
import csv
import turtle


class Base:
    '''
        Defines the Base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' initializes the object'''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns the JSON string representation of list_dictionaries '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes the JSON string representation of list_objs to a file '''
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = "{}.json".format(class_name)
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of objects represented by json_string '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Returns an instance with all attributes already set '''
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances from a file '''
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**dicts) for dicts in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' Serializes list_objs to CSV file '''
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = "{}.csv".format(class_name)

        with open(filename, 'w', newline='') as file:
            csv_writes = csv.writer(file)
            for obj in list_objs:
                if class_name == 'Rectangle':
                    csv_writes.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                        )
                elif class_name == 'Square':
                    csv_writes.writerow(
                        [obj.id, obj.size, obj.x, obj.y]
                        )

    @classmethod
    def load_from_file_csv(cls):
        ''' Deserializes CSV file to a list of instances '''
        class_name = cls.__name__
        filename = "{}.csv".format(class_name)

        try:
            with open(filename, 'r') as file:
                csv_reads = csv.reader(file)
                instances = []
                for row in csv_reads:
                    if class_name == 'Rectangle':
                        instances.append(cls.create(
                            id=int(row[0]),
                            width=int(row[1]), height=int(row[2]),
                            x=int(row[3]), y=int(row[4]))
                            )
                    elif class_name == 'Square':
                        instances.append(cls.create(
                            id=int(row[0]), size=int(row[1]),
                            x=int(row[2]), y=int(row[3])))
        except FileNotFoundError:
            return []

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' Opens a window and draws all
            Rectangles and Squares using
            Turtle graphics
        '''

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)
            turtle.right(90)
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)
            turtle.right(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        turtle.done()
