#!/usr/bin/python3.5
"""Modules that multiply two valid matrix
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies two valid matrixes

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        result  multiplication of two matrix


    """

    return (np.matmul(m_a, m_b))
