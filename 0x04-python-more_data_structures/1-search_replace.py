#!/usr/bin/python3
def search_replace(my_list, search, replace):
    upd = []
    for i in my_list:
        if i == search:
            upd.append(replace)
        else:
            upd.append(i)
    return upd
