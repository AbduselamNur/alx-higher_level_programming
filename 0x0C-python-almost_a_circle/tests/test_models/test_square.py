#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_one_arg(self):
        s = Square(1)
        self.assertEqual(s.width, 1)

    def test_square_two_arg(self):
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
