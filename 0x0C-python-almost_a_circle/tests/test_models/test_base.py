#!/usr/bin/python3
"""Defines unittests for base.py."""

import os
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unittests for testing Base class."""

    def test_default_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_given_id(self):
        b1 = Base(12)
        b2 = Base(12)
        self.assertEqual(b1.id, b2.id)

    def test_auto_increment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_to_json_string(self):
        b = Base()
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual('[{"id": 1}]', Base.to_json_string([b.to_dictionary()]))

    def test_from_json_string(self):
        self.assertEqual([], Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string("[]"))
        b = Base(1)
        json_string = '[{"id": 1, "x": 0, "y": 0, "width": 1, "height": 1}]'
        self.assertEqual([b], Base.from_json_string(json_string))

    def test_save_to_file(self):
        b = Base(1)
        Base.save_to_file([b])
        self.assertTrue(os.path.exists("Base.json"))

    def test_load_from_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        loaded_objs = Base.load_from_file()
        self.assertEqual([b1, b2], loaded_objs)

    def test_save_to_file_csv(self):
        b = Base(1)
        Base.save_to_file_csv([b])
        self.assertTrue(os.path.exists("Base.csv"))

    def test_load_from_file_csv(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file_csv([b1, b2])
        loaded_objs = Base.load_from_file_csv()
        self.assertEqual([b1, b2], loaded_objs)

    def test_create(self):
        dictionary = {'id': 1, 'x': 0, 'y': 0, 'width': 1, 'height': 1}
        b = Base.create(**dictionary)
        self.assertEqual(1, b.id)
        self.assertEqual(0, b.x)
        self.assertEqual(0, b.y)
        self.assertEqual(1, b.width)
        self.assertEqual(1, b.height)

if __name__ == "__main__":
    unittest.main()
