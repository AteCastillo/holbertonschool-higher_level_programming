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
