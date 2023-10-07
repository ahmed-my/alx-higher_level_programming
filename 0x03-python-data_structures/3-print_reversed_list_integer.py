#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        length = len(my_list)
        for i in range(length):
            print("{:d}".format(my_list[i]))
