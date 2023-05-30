#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0

    for i in range(1, 4):
        if i > a:
            raise Exception('Too far')

        res = res + a ** b // i

    res = res + b

    return res
