#!/usr/bin/python3
"""Unittesting Module"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    def test_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_not_none(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

