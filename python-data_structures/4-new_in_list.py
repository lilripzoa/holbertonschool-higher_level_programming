#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    mn_list = my_list[:]
    mn_list[idx] = element
    return mn_list