#!/usr/bin/python3
"""
Unittest for State class.
"""
import unittest
from models.city import City


class City_Test(unittest.TestCase):
    """
    Tests for State class
    """
    def setUp(self):
        """This is the set up function."""
        self.city = City()

    def test_attributes_existence(self):
        """This function tests for attributes_existence"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_is_string(self):
        """This function tests if id is a string"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

if __name__ == '__main__':
    unittest.main()
