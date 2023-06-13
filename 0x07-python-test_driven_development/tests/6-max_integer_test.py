#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class"""


    def test_empthy(self):
        self.assertEqual(max_integer([]), None)
    def test_end(self):
        self.assertEqual(max_integer([10, 2, 3, 40]), 40)
