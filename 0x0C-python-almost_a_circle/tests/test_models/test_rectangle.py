#!/usr/bin/python3
"""Defines unittests for rectangle.py."""

import os
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """Unittests for testing Rectangle class."""

    def test_init(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsInstance(r, Base)
        self.assertEqual(r.id, 1)

    def test_custom_id(self):
        r = Rectangle(10, 20, 0, 0, 5)
        self.assertEqual(r.id, 5)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 20)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "invalid")

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "invalid")

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 0, "invalid")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, -20)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -5)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 0, -5)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with self.assertLogs(level="INFO") as cm:
            r.display()
            self.assertEqual(cm.output, expected_output)

    def test_str(self):
        r = Rectangle(10, 20, 5, 6, 7)
        expected_output = "[Rectangle] (7) 5/6 - 10/20"
        self.assertEqual(str(r), expected_output)

    def test_update_args(self):
        r = Rectangle(10, 20)
        r.update(1, 15, 25, 5, 6)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_update_kwargs(self):
        r = Rectangle(10, 20)
        r.update(id=1, width=15, height=25, x=5, y=6)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 5, 6, 7)
        expected_dict = {'id': 7, 'width': 10, 'height': 20, 'x': 5, 'y': 6}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
