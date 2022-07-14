#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        print("{:d}.format(idx)")
    if idx < 0:
        print("None")
    if idx > len(my_list):
        print("None")
