#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_to_json_string_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

class TestBase_from_json_string(unittest.TestCase):
    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

class TestBase_to_json_string(unittest.TestCase):
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)
    def test_to_json_string_square_type(self):
        s = Square(4, 7, 9, 6)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))
    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)
    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))
    
    def test_to_json_string_none(self):
       self.assertEqual("[]", Base.to_json_string(None))
    
    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()
    
    def test_to_json_string_more_than_max_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)



