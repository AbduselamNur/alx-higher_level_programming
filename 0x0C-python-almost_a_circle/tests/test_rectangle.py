#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestReactangle(unittest.TestCase):
    def test_two_arg(self):
        r = Rectangle(1, 2)

        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_3_arg(self):
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
