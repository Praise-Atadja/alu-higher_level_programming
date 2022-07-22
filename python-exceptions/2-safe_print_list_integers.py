#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end=""))
        except(IndexError, ValueError):
            pass
        else:
            number += 1

        print("")
        return number