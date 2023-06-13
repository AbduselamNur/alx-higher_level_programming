#!/usr/bin/python3
"""Module that mutliply two valid Matrix"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies two valid matrices

    Args:
        m_a: first matrix
        m_b: second matric

    Returns:
        multiplication of two matrix

    Raises:
        TypeError: if m_a or m_b aren't a list
                   if m_a or m_b aren't a list of a lists
                   if the lists of m_a or m_b don't have integers or floats
                   if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiple
                    if m_a or m_b are empty
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")

    for elems in m_b:
        if not isinstance(elems, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    le = 0

    for elems in m_a:
        if le != 0 and le != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        le = len(elems)

    le = 0

    for elems in m_b:
        if le != 0 and le != len(elems):
            raise TypeError("each row of m_b must be of the same size")
        le = len(elems)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r_1 = []
    i_1 = 0

    for a in m_a:
        r_2 = []
        i_2 = 0
        num = 0
        while (i_2 < len(m_b[0])):
            num += a[i_1] * m_b[i_1][i_2]
            if i_1 == len(m_b) - 1:
                i_1 = 0
                i_2 += 1
                r_2.append(num)
                num = 0
            else:
                i_1 += 1
        r_1.append(r_2)

    return r_1
