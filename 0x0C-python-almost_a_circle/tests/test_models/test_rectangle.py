#!/usr/bin/python3
import unittest
import sys
import io
import os
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

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_with_x_y(self):
        out = io.StringIO()
        sys.stdout = out
        self.rect3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "\n\n\n\n   #\n   #\n")

    def test_display_without_x_y(self):
         out = io.StringIO()
         sys.stdout = out
         self.rect1.display()
         sys.stdout = sys.__stdout__
         self.assertEqual(out.getvalue(), "#\n#\n")

    def test_display_without_y(self):
        out = io.StringIO()
        sys.stdout = out
        self.rect2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "   #\n   #\n")

    def test_to_dictionary(self):
        self.assertEqual(self.rect1.to_dictionary(), {'id': 60, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

    def test_update(self):
        self.rect1.update()
        self.assertEqual(self.rect1.width, 1)

    def test_update_empty(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))

    def test_creat(self):
        r = Rectangle.create(**{ 'id': 89})
        self.assertEqual(r.id, 89)

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertEqual(os.path.getsize("Rectangle.json"), 2)

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertEqual(os.path.getsize("Rectangle.json"), 2)

    def test_save_to_file(self):
        r1 = Rectangle(1, 2)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 47, "width": 1, "height": 2, "x": 0, "y": 0}]')

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())


