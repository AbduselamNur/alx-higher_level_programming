#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestReactangle(unittest.TestCase):
    def test_two_arg(self):
        r_1 = Rectangle(1, 2)
        r_2 = Rectangle(3, 4)

        self.assertEqual(r_1.id, r_2.id - 1)
