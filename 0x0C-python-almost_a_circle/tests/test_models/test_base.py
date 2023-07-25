#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
