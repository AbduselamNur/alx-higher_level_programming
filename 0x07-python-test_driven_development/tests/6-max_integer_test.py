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
    def test_mid(self):
        self.assertEqual(max_integer([12, 33, 565, 34, 45]), 565)
    def test_neg(self):
        self.assertEqual(max_integer([-1, -2, -4, -10]), -1)
    def test_one(self):
        self.assertEqual(max_integer([100]), 100)
