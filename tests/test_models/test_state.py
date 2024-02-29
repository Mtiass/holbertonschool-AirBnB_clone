#!/usr/bin/python3
"""
Unittest for State class.
"""
import unittest
from models.state import State


class State_Test(unittest.TestCase):
    """
    Tests for State class
    """
    def setUp(self):
        """This is the set up function."""
        self.state = State()

    def test_attributes_existence(self):
        """This function tests for attributes_existence"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_is_string(self):
        """This function tests if id is a string"""
        self.assertIsInstance(self.state.name, str)

if __name__ == '__main__':
    unittest.main()
