#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for j in range(x):
            print(my_list[j], end="")
            number += 1
    except IndexError:
        pass
    print("")
    return (number)
