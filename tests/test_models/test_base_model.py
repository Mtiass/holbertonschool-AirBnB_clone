#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from time import sleep


class BaseModel_Test(unittest.TestCase):
    """
    Tests for BaseModel class
    """
    def test_00_class_type(self):
        """Test for correct class type"""
        b = BaseModel()
        self.assertEqual(b.__class__.__name__, "BaseModel")

    def test_save(self):
        """Test to validate that updated_at is changed when saved"""
        b = BaseModel()
        first_time = b.updated_at
        sleep(.5)
        b.save()
        second_time = b.updated_at
        self.assertNotEqual(first_time, second_time)


if __name__ == '__main__':
    unittest.main()
