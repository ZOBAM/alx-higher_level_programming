#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    y = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            y += 1
        except IndexError:
            break
        print('')
        return y
