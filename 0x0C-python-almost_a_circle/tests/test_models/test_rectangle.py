#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(1, 2)
        self.rect2 = Rectangle(1, 2, 3)
        self.rect3 = Rectangle(1, 2, 3, 4)

    def test_attributes(self):
        self.assertEqual(self.rect1.width, 1)
        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect1.y, 0)
        self.assertEqual(self.rect2.width, 1)
        self.assertEqual(self.rect2.height, 2)
        self.assertEqual(self.rect2.x, 3)
        self.assertEqual(self.rect2.y, 0)
        self.assertEqual(self.rect3.width, 1)
        self.assertEqual(self.rect3.height, 2)
        self.assertEqual(self.rect3.x, 3)
        self.assertEqual(self.rect3.y, 4)

    def test_err(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 3, -2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -2)

    def test_five_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(5, r.id)
