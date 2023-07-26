#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square(self):
        s = Square(1)
        self.assertEqual(s.width, 1)
