#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    my_list = my_list.copy()
    if idx < 0:
        return (my_list.copy())
    elif idx > length - 1:
        return (my_list.copy())
    else:
        my_list[idx] = element
        return (my_list)
