#!/usr/bin/python3
"""
Unittest for Amenity class.
"""
import unittest
from models.amenity import Amenity

class Amenity_Test(unittest.TestCase):
    """
    Tests for Amenity class
    """
    def setUp(self):
        """This is the set up function."""
        self.amenity = Amenity()

    def test_attributes_existence(self):
        """This function tests for attributes_existence"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_is_string(self):
        """This function tests if id is a string"""
        self.assertIsInstance(self.amenity.name, str)

if __name__ == '__main__':
    unittest.main()
