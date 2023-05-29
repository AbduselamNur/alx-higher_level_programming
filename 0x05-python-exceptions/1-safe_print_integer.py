#!/usr/bin/python3
def safe_print_integer(value):
    if value is None:
        return 0
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except ValueError:
        pass
