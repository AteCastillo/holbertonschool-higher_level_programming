#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        lists = []
        for a in my_list:
            if a % 2 == 0:
                lists.append(True)
            else:
                lists.append(False)  #list comprehension
        return(lists)           