#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_integer = set(my_list)
    add = 0

    for num in uniq_integer:
        add += num

    return (add)
