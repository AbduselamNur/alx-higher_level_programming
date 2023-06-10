#!/usr/bin/python3
"""This Module is Add to Number"""

def add_integer(a, b=98):
    """
    function that return the the sum

    Args:
        a (int): integer the first digit
        b (int): integer the second digit defualt: 98

    raise:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Return: 
        a + b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
