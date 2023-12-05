#!/usr/bin/python3
'''
    Student to JSON
'''


class Student:
    '''
        defines a student
    '''

    def __init__(self, f_name, l_name, age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age

    def to_json(self, attrs):
        the_dict = self.__dict__
        if attrs is None:
            return the_dict
        return {i: the_dict[i] for i in attrs if i in the_dict}
