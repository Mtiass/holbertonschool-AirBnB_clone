#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import unittest
from models.base_model import BaseModel


class BaseModel_Test(unittest.TestCase):
    """
    Tests for BaseModel class
    """
    def test_00_class_type(self):
        """Test for correct class type"""
        b = BaseModel()
        self.assertEqual(b.__class__.__name__, "BaseModel")


if __name__ == '__main__':
    unittest.main()
