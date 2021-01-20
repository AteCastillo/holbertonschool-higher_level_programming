#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    my_list.sort()
    return my_list[-1]
  #  max = my_list[0]  # Assume first number in list is largest
    # initially and assign it to variable "max"
   # for i in my_list:
    #    if i > max: #it is possible to put my_list[i] or just i
     #       max = i
    # return(max)
