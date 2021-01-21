#!/usr/bin/python3
"""documentation"""


class Student:
    """new class"""

    def __init__(self, first_name, last_name, age):
        """instantiate"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """return dict"""
        return self.__dict__

    def to_json(self, attrs=None):
        """retrieves a dictionary"""
        if attrs is not None:
            new_dict = {}
            for obj in attrs:
                if type(obj) is not str:
                    return self.__dict__
            # for obj in attrs:
                if obj in self.__dict__:
                    new_dict[obj] = self.__dict__[obj]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces the atributes of a dict"""
        for key, value in json.items():
            self.__dict__[key] = value
