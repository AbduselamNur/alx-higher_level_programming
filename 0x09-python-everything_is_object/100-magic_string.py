#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "x", getattr(magic_string, "x", 0) + 1)
    return ("BestSchool, " * getattr(magic_string, "x", 0))[:-2]
