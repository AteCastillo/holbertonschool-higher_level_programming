#!/usr/bin/python3
"""new file"""


def read_file(filename=""):
    """to read file"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
