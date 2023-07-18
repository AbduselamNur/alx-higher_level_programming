#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestReactangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(1, 2)

        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
