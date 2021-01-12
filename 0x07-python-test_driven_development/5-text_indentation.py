#!/usr/bin/python3
"""
a function that prints a text
 with 2 new lines after each
 of these characters: ., ? and :
"""


def text_indentation(text):
    """
    text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_list = list(text)
    for i in range(len(new_list)):
        if new_list[i] is ".":
            new_list[i + 1] = '\n\n'
        if new_list[i] is "?":
            new_list[i + 1] = '\n\n'
        if new_list[i] is ":":
            new_list[i + 1] = '\n\n'
    new_tab = ""
    new_tab = new_tab.join(new_list)
    print("{}".format(new_tab), end="")
