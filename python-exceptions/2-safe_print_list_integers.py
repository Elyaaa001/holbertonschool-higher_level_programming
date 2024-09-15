#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed_count = 0
    try:
        while count < x:
            value = my_list[count]
            if isinstance(value, int):
                print("{:d}".format(value), end='')
                printed_count += 1
            count += 1
    except IndexError:
        pass
    print()
    return printed_count
