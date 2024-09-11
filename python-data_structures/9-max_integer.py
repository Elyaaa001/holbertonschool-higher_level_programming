#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in my_list:
        largest = my_list[0]
        if i > largest:
            largest = i
    return largest
