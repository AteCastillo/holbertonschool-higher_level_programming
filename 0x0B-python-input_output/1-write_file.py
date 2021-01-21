#!/usr/bin/python3
"""more files"""


def write_file(filename="", text=""):
    """to write a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
