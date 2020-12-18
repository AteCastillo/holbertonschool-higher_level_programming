#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    count = 0
    for i in new_list:
        if i == search:
            new_list[count] = replace
        count += 1
# new_list.append(replace)
# else:
# new_list.append(i)
    return new_list
