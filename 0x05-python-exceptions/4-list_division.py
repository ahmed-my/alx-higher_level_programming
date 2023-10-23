#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []

    for n in range(list_length):
        try:
            div = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print("Division by zero")
            div = 0
        except (TypeError, IndexError):
            print("An error occurred")
            div = 0
        finally:
            my_list.append(div)

    return my_list
