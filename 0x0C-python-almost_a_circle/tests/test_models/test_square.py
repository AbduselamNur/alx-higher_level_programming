#!/usr/bin/python3
import unittest
import os
import sys
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle

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

    def test_square_four_arg(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_str(self):
        s = Square(1, 1, 1, 1)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")

    def test_to_dictionary(self):
        s = Square(1, 1, 1, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'x': 1, 'size': 1, 'y': 1,})

    def test_update(self):
        s = Square(1)
        s.update()
        self.assertEqual(s.size, 1)

    def test_update_empty(self):
        s = Square(1, 1, 1, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")

    def test_create(self):
        s = Square.create(**{ 'id': 89 })
        self.assertEqual(s.id, 89)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')

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
    def test_square_first_neg(self):
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_square_second_neg(self):
        with self.assertRaises(ValueError):
            s = Square(1, -2)

    def test_square_third_neg(self):
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_square_zero(self):
        with self.assertRaises(ValueError):
            s = Square(0)

class TestBase_save_to_file(unittest.TestCase):
    @classmethod
    def tearDown(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_one(self):
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 66, "size": 1, "x": 0, "y": 0}]')
