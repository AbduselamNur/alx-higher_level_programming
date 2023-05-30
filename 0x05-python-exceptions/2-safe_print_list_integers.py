#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return 0
    leng = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            leng += 1
        except (IndexError, ValueError):
            pass
    print()
    return leng
