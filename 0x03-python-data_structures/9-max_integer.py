#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    max = my_list[0]  # Assume first number in list is largest
    # initially and assign it to variable "max"
    for i in my_list:
        if i > max:
            max = i
    return(max)
