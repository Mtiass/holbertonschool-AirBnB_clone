#!/usr/bin/python3
"""
Unittest for Review class.
"""
import unittest
from models.review import Review


class Amenity_Test(unittest.TestCase):
    """
    Tests for Review class
    """
    def setUp(self):
        """This is the set up function."""
        self.review = Review()

    def test_attributes_existence(self):
        """This function tests for attributes_existence"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_is_string(self):
        """This function tests if id is a string"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

if __name__ == '__main__':
    unittest.main()
