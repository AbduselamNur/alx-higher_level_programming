#!/usr/bin/python3
"""Module That Find A Peak"""


def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    peak = list_of_integers[0]
    for i in list_of_integers:
        if i >= peak:
            peak = i
    return peak
