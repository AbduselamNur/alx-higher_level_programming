#!/usr/bin/python3
def uniq_add(my_list=[]):
    common = set(my_list)
    add = 0
    for i in common:
        add += i
    return add
