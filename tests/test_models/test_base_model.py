#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from time import sleep
from datetime import datetime
from unittest.mock import patch


class BaseModel_Test(unittest.TestCase):
    """
    Tests for BaseModel class
    """
    def setUp(self):
        """This is the set up function."""
        self.base_model = BaseModel()

    def test_class_type(self):
        """This function tests for correct class type"""
        b = BaseModel()
        self.assertEqual(b.__class__.__name__, "BaseModel")

    def test_attributes_existence(self):
        """This function tests for attributes_existence"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        """This function tests if id is a string"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """This function tests if created_at is a datetime"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """This function tests if updated_at is a datetime"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """This function tests to validate that updated_at is changed when
        saved"""
        b = BaseModel()
        first_time = b.updated_at
        sleep(.5)
        b.save()
        second_time = b.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_save_updates_updated_at(self):
        """This function tests if save updates updated_at"""
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        """This function tests if to_dict returns a dict"""
        result = self.base_model.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_includes_class_name(self):
        """This function tests if to_dict includes class name"""
        result = self.base_model.to_dict()
        self.assertIn('__class__', result)
        self.assertEqual(result['__class__'], 'BaseModel')

    def test_to_dict_includes_created_at_isoformat(self):
        """This function tests if to_dict includes created at isoformat"""
        result = self.base_model.to_dict()
        self.assertIn('created_at', result)
        self.assertEqual(result['created_at'],
                         self.base_model.created_at.isoformat())

    def test_to_dict_includes_updated_at_isoformat(self):
        """This function tests if to_dict includes updated at isoformat"""
        result = self.base_model.to_dict()
        self.assertIn('updated_at', result)
        self.assertEqual(result['updated_at'],
                         self.base_model.updated_at.isoformat())

    def test_str_representation(self):
        """This function tests the str representation"""
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    @patch('uuid.uuid4')
    def test_id_is_set_on_instance_creation(self, mock_uuid4):
        """This function tests if id is set on instance creation"""
        mock_uuid4.return_value = 'mocked_uuid'
        base_model = BaseModel()
        self.assertEqual(base_model.id, 'mocked_uuid')


if __name__ == '__main__':
    unittest.main()
