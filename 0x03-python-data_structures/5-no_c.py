#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for ch in my_string:
        if len(my_string) <= 0:
            return None
        elif ch != "c" and ch != "C":
            new += ch
    return new
