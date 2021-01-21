#!/usr/bin/python3
"""new task"""


def append_write(filename="", text=""):
    """to append"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
