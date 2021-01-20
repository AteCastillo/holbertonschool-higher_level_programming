#!/usr/bin/python3
def best_score(a_dictionary):
    values = 0
    key1 = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return
    for key, value in a_dictionary.items():
        if value > values:
            key1 = key
            values = value
    return key1