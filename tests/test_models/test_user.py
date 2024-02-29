#!/usr/bin/python3
"""
Unittest for User class.
"""
import unittest
from models.user import User


class User_Test(unittest.TestCase):
    """
    Tests for User class
    """
    def setUp(self):
        """This is the set up function."""
        self.user = User()

    def test_attributes_existence(self):
        """This function tests for attributes_existence"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_is_string(self):
        """This function tests if id is a string"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

if __name__ == '__main__':
    unittest.main()
