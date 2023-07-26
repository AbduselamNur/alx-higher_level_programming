#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_one_arg(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_two_arg(self):
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_three_arg(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

class TestSquareErr(unittest.TestCase):
    def test_square_first_str(self):
        with self.assertRaises(TypeError):
            s = Square("1")

    def test_square_second_str(self):
        with self.assertRaises(TypeError):
            s = Square(1, "2")
    def test_square_third_str(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")
