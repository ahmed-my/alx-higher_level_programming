#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ Delete an item at a specific position in a list."""
    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return (my_list)
    else:
        del my_list[idx]
        return (my_list)
