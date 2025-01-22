#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = []
    total = 0

    for i in my_list:
        if i not in res:
            res.append(i)
            total += i
    return total
