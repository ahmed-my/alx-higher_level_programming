#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for n in range(x):
        try:
            if isinstance(my_list[n], int):
                print("{:d}".format(my_list[n]), end="")
                num += 1
        except (ValueError, TypeError):
            pass
    print()
    return (num)
