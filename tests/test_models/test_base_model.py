#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from time import sleep
from datetime import datetime
from models.engine.file_storage import FileStorage
import os
import json
from unittest import mock


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

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates."""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

    def test_save(self):
        """This function tests to validate that updated_at is changed when
        saved"""
        b = BaseModel()
        first_time = b.updated_at
        sleep(.5)
        b.save()
        second_time = b.updated_at
        self.assertNotEqual(first_time, second_time)

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

    def test_init_with_kwargs_sets_attributes(self):
        """This function tests initialization with kwargs sets attributes"""
        kwargs = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00.0',
            'updated_at': '2022-01-02T00:00:00.0',
            'other_attr': 'value'
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, 'test_id')
        self.assertEqual(base_model.created_at, datetime(2022, 1, 1))
        self.assertEqual(base_model.updated_at, datetime(2022, 1, 2))
        self.assertTrue(hasattr(base_model, 'other_attr'))

    def test_init_with_empty_kwargs_generates_attributes(self):
        """This function tests initialization with empty kwargs generates
        attributes"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
